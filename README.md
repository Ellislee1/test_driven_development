# Test Driven Development
---
This repo serves as a simplified example to unit test with `pytest` and basic CI/CD workflows with github actions.
It is by no means a comprehensive or fully correct implementation but serves as a starting point from my point of view.

## Prerequisites
Before starting it is recommended that flake8 and black is installed and set up. For this program we allow 120 characters per line and both flake8 and black are setup as such globally.

it is assumed the python, black and flake8 addons are installed.

To access these settings on VS-code press `ctrl+,`:
### Black
For Black, under the user tab searck `Black-formatter:Args`. Press `Add Item` and enter `--line-length` and press `OK`.
Then Press `Add Item` again and enter `120` followed by pressing `OK`.
### flake8
For flake8, similarly search `Flake8` and scroll down until you reack `Flake8:Args`.
Press `Add Item` and enter `--max-line-length` then press `OK`.
Press `Add Item` again and enter `120` then press `OK`.

---
## CI/CD Github Actions
## Linter
The linter action is setup to run in the file `.github/workflows/linter.yml` which looks like:
```yml
# This workflow executes several linters on changed files based on languages used in your code base whenever
# you push a code or open a pull request.
#
# You can adjust the behavior by modifying this file.
# For more information, see:
# https://github.com/github/super-linter
name: Lint Code Base

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
jobs:
  run-lint:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        with:
          # Full git history is needed to get a proper list of changed files within `super-linter`
          fetch-depth: 0

      - name: Lint Code Base
        uses: github/super-linter@v4
        env:
          VALIDATE_ALL_CODEBASE: true
          VALIDATE_PYTHON_FLAKE8: true
          DEFAULT_BRANCH: "main"
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
It uses the `.flake8` file to adjust the parameters:
```
[flake8]
max-line-length = 120
```
