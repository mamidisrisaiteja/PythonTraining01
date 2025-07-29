import pytest


@pytest.fixture(scope='session')
def test_session_setup():
    print("session setup is done")


@pytest.fixture(scope='function')
def test_initial_setup():
    print("Initial setup is done")

@pytest.fixture(scope='function')
def test_tear_down():
    yield
    print("Exit setup is done")

@pytest.fixture(scope='class')
def test_class_setup():
    print("Initial setup is done for class test")