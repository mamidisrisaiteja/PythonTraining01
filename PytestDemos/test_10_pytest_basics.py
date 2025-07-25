import pytest


@pytest.fixture(scope='module')
def test_first_fixture():
    print("in my first setup")
    return True

def test_first(test_first_fixture):
    print("Running first test")
    assert test_first_fixture is True