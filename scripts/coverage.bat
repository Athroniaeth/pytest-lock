poetry run coverage run --source=src -m pytest
poetry run coverage report -m --fail-under=50
poetry run coverage html
