# Installation

## Setup uv
Select one of the following methods for installing uv

1. PyPI
```bash
pip install uv
```
2. WinGet
```bash
winget install --id=astral-sh.uv  -e
```
3. homebrew
```bash
brew install uv
```

## Initialize project: method 1

### 1. Create project.
```bash
uv init --python 3.12
```
### 2. Installing dependencies
```bash
uv add -r requirements.txt
```
### 3. Installing chromium browser
```bash
playwright install --with-deps chromium
```

## Initialize project: method 2
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
uvx playwright install chromium --with-deps
or
playwright install --with-deps chromium
or
playwright install chromium
```