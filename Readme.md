# DeviseConverter

A PySide6 (Qt) desktop application for real-time currency conversion using the `currency-converter` library.

## Features
- Real-time currency conversion using ECB exchange rates
- Simple GUI with combo boxes for currency selection
- Spin boxes for amount input/output
- Invert button to swap currencies
- Dark theme interface

## Installation & Usage

### Local Development
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (note: requirement.txt not requirements.txt)
pip install -r requirement.txt

# Run the application
python app/app.py
```

### Docker Deployment
```bash
# Build and run using Docker Compose
docker-compose up --build

# The GUI will appear on your host machine's display
```

## Project Structure
```
app/app.py          # Main application (~90 lines)
requirement.txt     # Dependencies: CurrencyConverter, PySide6
Dockerfile          # Docker build configuration
docker-compose.yml  # Docker Compose deployment file
sonar-project.properties  # SonarCloud configuration
.github/workflows/build.yml  # CI: SonarCloud scan on push/PR to master
```

## Technical Details
- **Python Version**: 3.11
- **GUI Framework**: PySide6 (Qt for Python)
- **Currency Data**: Fetched from European Central Bank via `currency_converter` library
- **UI Components**: 
  - Two QComboBox widgets (from/to currency)
  - Two QSpinBox widgets (amount/converted amount)
  - QPushButton for currency inversion
  - Dark theme styling

## Important Notes
- Dependency file is `requirement.txt` (singular), not `requirements.txt`
- `QSpinBox` used for amounts — only handles integers (no decimals)
- No error handling for network failures when fetching exchange rates
- For Docker GUI display to work, you need an X11 server running on your host:
  - Linux: Usually pre-installed
  - macOS: Install XQuartz
  - Windows: Install VcXsrv or similar X server

## CI/CD
- SonarCloud scan runs on push/PR to `master` branch
- Requires `SONAR_TOKEN` secret in GitHub