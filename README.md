# Installation

## Window

### Setup uv for window
Select one of the following methods for installing uv

- PyPI
```bash
pip install uv
```
- WinGet
```bash
winget install --id=astral-sh.uv  -e
```

### Initialize project for window
```bash
uv venv --python 3.12
```
```bash
.venv\Scripts\activate
```
```bash
uv pip install -r requirements.txt
```
```bash
uvx playwright install chromium
```

## Mac

### Setup uv for window
Select one of the following methods for installing uv

- PyPI
```bash
pip install uv
```
- WinGet
```bash
winget install --id=astral-sh.uv  -e
```
- homebrew
```bash
brew install uv
```

### Initialize project for Mac
```bash
uv venv --python 3.12
```
```bash
source .venv/bin/activate
```
```bash
uv pip install -r requirements.txt
```
```bash
uvx playwright install chromium
```
