# GEMINI.md - Project Context: DeviseConverter

## Project Overview
**DeviseConverter** is a Python-based desktop application for real-time currency conversion. It features a graphical user interface (GUI) built with **PySide6 (Qt for Python)** and uses the `currency-converter` library to fetch exchange rates from the European Central Bank.

### Key Technologies
- **Language:** Python 3.11
- **GUI Framework:** PySide6 (6.6.0)
- **Data Source:** `currency-converter` (ECB data)
- **Containerization:** Docker, Docker Compose
- **Deployment:** Dokploy (via Webtop for browser-based GUI access)
- **CI/CD:** GitHub Actions with SonarCloud analysis

### Architecture
The project follows a simple single-module architecture:
- `app/app.py`: Contains the `App` class (inheriting from `QTabWidget`) which handles UI layout, logic, and currency conversion.
- `requirement.txt`: Lists all Python dependencies.
- `Dockerfile`: Configures a Python environment with necessary system libraries for Qt/GUI execution.

## Building and Running

### Local Development (Native)
```bash
# 1. Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies (Note: file is singular 'requirement.txt')
pip install -r requirement.txt

# 3. Run application
python app/app.py
```

### Local Development (Docker)
Requires an X11 server (XQuartz on macOS, VcXsrv on Windows) to display the GUI.
```bash
docker-compose up --build
```

### VPS Deployment (Dokploy)
The application is deployed using a "Webtop" approach to allow GUI interaction via a web browser.
- **Config:** `dokploy.yml`
- **Access:** `http://<vps-ip>:3000`
- **Execution:** Inside the Webtop terminal:
  ```bash
  cd /app && pip install -r requirement.txt && python3 app/app.py
  ```

## Development Conventions

### Coding Style & Standards
- **Naming:** Follows standard Python conventions, but uses some Hungarian-style prefixes for UI widgets (e.g., `cbb_` for QComboBox, `spn_` for QSpinBox, `btn_` for QPushButton).
- **Styling:** The application uses a hardcoded dark theme via `setStyleSheet` in `app/app.py`.
- **UI Logic:** Logic is centralized in the `App` class. Signals (like `activated` or `valueChanged`) are connected to the `compute` method for real-time updates.

### Important Notes
- **Dependency File:** Always use `requirement.txt` (not `requirements.txt`).
- **Precision:** Uses `QSpinBox` for amounts, which limits inputs and outputs to **integers**.
- **Error Handling:** Currently lacks robust error handling for network issues during currency data fetching.
- **CI:** SonarCloud scans are triggered on every push to the `master` branch.

## TODOs / Future Improvements
- [ ] Implement decimal support by switching to `QDoubleSpinBox`.
- [ ] Add unit tests for the conversion logic.
- [ ] Add error handling for offline mode or API failures.
- [ ] Implement a more robust theme management system.
