from PySide6 import QtWidgets as qt
from currency_converter import CurrencyConverter
from PySide6 import QtGui as qg


class App(qt.QTabWidget):
    def __init__(self ):
        super().__init__()
        self.currency = CurrencyConverter()
        self.setWindowTitle("Devise Converter")
        self.setup_ui()
        self.set_default_values()
        self.setup_connections()
        self.setup_css()

    def setup_ui(self):
        self.layout = qt.QHBoxLayout(self) # type:ignore 
        self.cbb_devisesFrom = qt.QComboBox()
        self.spn_montant = qt.QSpinBox()

        self.cbb_devisesTo = qt.QComboBox()
        self.spn_montantConverted = qt.QSpinBox()

        self.btn_inverse = qt.QPushButton('Inverser devise')

        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverted)
        self.layout.addWidget(self.btn_inverse) 

    def set_default_values(self):
        sorted_devises = sorted(list(self.currency.currencies))  # type:ignore
       
        self.cbb_devisesFrom.addItems(sorted_devises)
        self.cbb_devisesTo.addItems(sorted_devises)

        self.cbb_devisesFrom.setCurrentText('EUR')
        self.cbb_devisesTo.setCurrentText('USD') 

        self.spn_montant.setRange(1, 1_000_000)
        self.spn_montantConverted.setRange(1, 1_000_000)
        self.spn_montant.setValue(100)
        self.spn_montantConverted.setValue(100)

    def setup_connections(self):
        self.cbb_devisesFrom.activated.connect(self.compute) 
        self.cbb_devisesTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverse.clicked.connect(self.inverse_devises)

    def compute(self):
        montant = self.spn_montant.value()
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()

        converted_currency = self.currency.convert(montant, devise_from, devise_to)
        self.spn_montantConverted.setValue(converted_currency)
        # print(montant, devise_from, devise_to)
        # print(f"{montant} {devise_from} = {converted_currency} {devise_to}") 

    def inverse_devises(self):
        # temp = self.cbb_devisesFrom.currentText()
        # self.cbb_devisesFrom.setCurrentText(self.cbb_devisesTo.currentText())
        # self.cbb_devisesTo.setCurrentText(temp)

        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        self.cbb_devisesFrom.setCurrentText(devise_to)
        self.cbb_devisesTo.setCurrentText(devise_from)

        self.compute()

    def setup_css(self):
        self.setStyleSheet("""
            background-color: black;
            color: white;
            """)

        





if __name__ == "__main__":
    app = qt.QApplication([]) # il faut une liste vide pour la classe QApplication

    window = App()
    window.show()

    app.exec_()