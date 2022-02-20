test:
	mypy src
	flake8 src

	mypy tests
	flake8 tests

	pytest
