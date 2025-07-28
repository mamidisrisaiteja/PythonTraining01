import pytest

@pytest.fixture(scope="module")

def test_second_fixture():

    print("in my first setup")

    yield

    print("perfomrning db conncetions closing after the test")

def test_first(test_second_fixture):

    print("Running first test")

def test_second(test_second_fixture):

    print("Running second test")

def test_third(test_second_fixture):

    print("Running third test")

