# Python OpenAI examples

## For development

### Initialise python virtal environment

- `python -m venv .`
- `source ./bin/activate`

### Install packages

- `pip install -r requirements.txt`

### Lint

- `python -m pylint src/`

### Style check

- `python -m black src/`

### Run unit tests

- Ensure `OPENAI_API_KEY` is set in the environment: `export OPENAI_API_KEY=<key>`
- `python -m pytest`

### Run unit tests and report coverage

- `python -m coverage run -m pytest && python -m coverage report`

### All in one line

- `python -m pylint src/ && python -m black src/ && python -m coverage run -m pytest && python -m coverage report`
