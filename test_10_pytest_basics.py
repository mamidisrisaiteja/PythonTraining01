import pytest

from _pytest import scope

@pytest.fixture(scope="module")

def test_second_fixture():

    print("in my first setup")

    yield

    print("performing db connections closing after the test")

def test_first(test_second_fixture):

    print("Running first test")

@pytest.mark.smoke

def test_second(test_second_fixture):

    print("Running second test")

@pytest.mark.skip

def test_third(test_second_fixture):

    print("Running third test")