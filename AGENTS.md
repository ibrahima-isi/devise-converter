# DeviseConverter - Agent Instructions

## Project Overview
PySide6 (Qt) desktop app for real-time currency conversion using `currency-converter` library. Python 3.11.

## Key Commands
```bash
# Install dependencies (note: requirement.txt not requirements.txt)
pip install -r requirement.txt

# Run application
python app/app.py
```

## Project Structure
```
app/app.py          # Main application (single file, ~90 lines)
requirement.txt     # Dependencies (CurrencyConverter, PySide6)
sonar-project.properties  # SonarCloud config
.github/workflows/build.yml  # CI: SonarCloud scan on push/PR to master
```

## Development Notes
- No test framework, linter, or type checker configured
- No virtual environment setup documented — create one manually
- Entry point: `App` class in `app/app.py` inherits from `QTabWidget`
- Currency data loaded from `currency_converter.CurrencyConverter()` (fetches ECB rates)
- UI: two combo boxes (from/to currency), two spin boxes (amount/converted), invert button
- Dark theme hardcoded in `setup_css()`

## CI/CD
- SonarCloud scan runs on push/PR to `master` branch
- Requires `SONAR_TOKEN` secret in GitHub

## Gotchas
- Dependency file is `requirement.txt` (singular), not `requirements.txt`
- `QSpinBox` used for amounts — only handles integers (no decimals)
- No error handling for network failures when fetching exchange rates