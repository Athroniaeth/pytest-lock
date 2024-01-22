from _pytest.pytester import Pytester


def test_lock_change_date_today(pytester: Pytester) -> None:
    """Test the creation of a cache."""
    pytester.copy_example("conftest.py")
    pytester.copy_example("scenarios/test_fixture_lock.py")

    result = pytester.runpytest("--lock", "--simulate")

    result.assert_outcomes(skipped=1)

    # Check if the lock is simulated (not created)
    path_cache = pytester.path / ".pytest_cache" / "cache" / "test_fixture_lock.json"
    assert not path_cache.exists()