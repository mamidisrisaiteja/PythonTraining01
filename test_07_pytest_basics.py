import pytest

@pytest.fixture

def initial_setup(scope="module"):

    print("Initial setup before tests")

def test_first(initial_setup):

    print("Running first test")

    assert True

def test_second(initial_setup):

    print("Running second test")

    assert True


