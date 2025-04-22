# Python OpenAI examples

## For development

### Install packages
- `pip install -r requirements.txt`

### Lint
- `pylint src/`

### Style check
- `black src/`

### Run unit tests
- Ensure `OPENAI_API_KEY` is set in the environment: `export OPENAI_API_KEY=<key>`
- `pytest`

### Run unit tests and report coverage
- `coverage run -m pytest && coverage report -m`

### All in one line
- `pylint src/ && black src/ && coverage run -m pytest && coverage report -m`