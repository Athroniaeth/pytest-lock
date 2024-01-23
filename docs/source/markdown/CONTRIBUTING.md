# Contributing
## How to contribute

### Git
Create a fork of the repository, then clone it locally. Make your changes, then push them to your fork. Finally, create a pull request from your fork to the main repository. Please detail what you would like to add, why you think it would be useful (no matter how small the modification, an addition for a better user experience, no matter how small, is always worthwhile).

### Poetry
This project uses poetry to manage dependencies. To install poetry, follow the instructions [here](https://python-poetry.org/docs/#installation). Once you have poetry installed, you can install the dependencies by running `poetry install` in the root directory of the project. Make your modification, in the cases where your add a functionnalities, please add tests and documentation. Once you are done, you can make a pull request.

### Pipeline CI/CD
This is not mandatory, but we would appreciate it if you would follow this sequence of orders before making a PR. This will save the project maintainers a lot of work and make it easier for them to maintain your contribution. A PR that does not follow this sequence of commands could fail the CI/CD pipeline tests (which execute the same sequence of instructions with different degrees of severity as we approach a development/production/version branch). It doesn't matter if it fails, it can always be corrected by you or a maintainer.
* __tests__: This project uses `pytest` to run tests. To run the tests, run `poetry run pytest` in the root directory of the project.
* __documentations__: This project uses `sphinx` to generate documentation. To generate the documentation, run `poetry run sphinx-build -b html docs docs/build` in the root directory of the project. The documentation will be in the `docs/build` directory.
* __linter__: This project uses `ruff` to lint the code. To lint the code, run `poetry run ruff` in the root directory of the project.
* __format__: This project also uses `ruff` to format the code. To format the code, run `poetry run ruff --format` in the root directory of the project.
* __typing__: This project uses `mypy` to type check the code. To type check the code, run `poetry run mypy` in the root directory of the project.

You can check most version of python with `poetry run tox`. This will run all the tests in all the version of python (if you have them installed).

## Reporting bugs
Before reporting bugs, go to the documentation in **know issues** to see if your problem is already known. If it is not, then you can report it in the issues tab. Please include the following information:
* What is the version of python you are using
* What version of the library you are using
* What is the OS you are using
* How we can reproduce the bug

## Suggesting enhancements
This is no different from fork creation and PR, except that you don't offer any code. In this case, we may not fully understand your proposal, as there is no code attached, so we must be careful to give enough details.

