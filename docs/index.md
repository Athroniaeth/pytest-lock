# pytest-lock

## Overview

[![Workflow](https://img.shields.io/github/actions/workflow/status/Athroniaeth/pytest-lock/release.yml)]("https://github.com/Athroniaeth/pytest-lock/actions/workflows/release.yml")
[![License MIT](https://img.shields.io/badge/license-MIT-blue)](https://codecov.io/gh/athroniaeth/pytest-lock)
[![Python versions](https://img.shields.io/pypi/pyversions/bandit.svg)](https://pypi.python.org/pypi/bandit)
[![PyPI version](https://badge.fury.io/py/bandit.svg)](https://badge.fury.io/py/bandit)
[![Security: Bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Documentation Status](https://readthedocs.org/projects/pytest-lock/badge/?version=latest)](https://pytest-lock.readthedocs.io/en/latest/)
[![codecov](https://codecov.io/gh/Athroniaeth/pytest-lock/graph/badge.svg?token=28E1OZ144W)](https://codecov.io/gh/Athroniaeth/pytest-lock)

**pytest-lock** is a pytest plugin that allows you to "lock" the results of unit tests, storing them in a local cache.
This is particularly useful for tests that are resource-intensive or don't need to be run every time. When the tests are
run subsequently. **pytest-lock** will compare the current results with the locked results and issue a warning if there
are any discrepancies.


```{warning}
This library is recent and may therefore contain a few bugs, and will change regularly until its first stable version. I don't recommend using it for serious projects, despite its code coverage.
```

## Installation

To install pytest-lock, you can use pip:

```bash
pip install pytest-lock
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Tutorials

./tutorials/lock.md
./tutorials/lock_simulate.md
./tutorials/lock_only_skip.md
./tutorials/lock_date.md
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Common problems

./common_problems/locking_collision.md
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Development

./markdown/ROADMAP.md
./markdown/CHANGELOG.md
./markdown/CONTRIBUTING.md
./markdown/CODE_OF_CONDUCT.md
```