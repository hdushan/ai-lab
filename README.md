# Python OpenAI examples

## For development

### Initialise python virtal environment

- `python -m venv .`
- `source ./bin/activate`
  OR
- `poetry env use 3.13`
- `eval $(poetry env activate)`

### Install packages

Prequisite: Have `pip` or `poetry` installed

- `pip install -r requirements.txt`
  OR
- `poetry install`

### Lint

- `python -m pylint src/`
  OR
- `poetry run pylint src/`

### Style check

- `python -m black src/ --check --diff --verbose`
  OR
- `poetry run black src/ --check --diff --verbose`

### Run unit tests

- Ensure `OPENAI_API_KEY` is set in the environment: `export OPENAI_API_KEY=<key>`
- `python -m pytest`
  OR
- `poetry pytest`

### Run unit tests and report coverage

- `python -m coverage run -m pytest && python -m coverage report`
  OR
- `poetry run coverage run -m pytest && poetry run coverage report`

### All in one line

- `python -m pylint src/ && python -m black src/ --check --diff --verbose && python -m coverage run -m pytest && python -m coverage report`
  OR
- `poetry run pylint src/ && poetry run black src/ --check --diff --verbose && poetry run coverage run -m pytest && poetry run coverage report`
