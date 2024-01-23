# pytest-lock

## Overview

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