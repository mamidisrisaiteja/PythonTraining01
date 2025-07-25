import pytest
from _pytest import scope

@pytest.fixture(scope="function")
def initial_setup_three():
    print("Initial setup three before tests")