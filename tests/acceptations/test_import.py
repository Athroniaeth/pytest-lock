def test_import_fixture():
    try:
        from pytest_lock import FixtureLock  # noqa: F401
    except ImportError:
        assert False, "Can't import 'FixtureLock' from 'pytest_lock'"
    else:
        assert True, "Can't import 'FixtureLock' from 'pytest_lock'"
