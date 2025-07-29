import pytest


@pytest.fixture(scope="class")

def initial_setup_two():
    print("Initial setup two before tests")
    
@pytest.mark.usefixtures("initial_setup_two")

class TestExample:
    def test_third(self):
        print("Running third test")
        assert True
    def test_fourth(self):
        print("Running fourth test")
        assert True