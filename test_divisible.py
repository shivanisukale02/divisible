import divisible
import pytest

@pytest.fixture
def input():
    a=25
    return a

def test_div5(input):
    #a=10
    result=divisible.div5(input)
    assert result==True


def test_div5_1(input):
    #a=12
    result=divisible.div5(input)
    assert result==False


def test_div7(input):
    #a = 14
    result = divisible.div7(input)
    assert result == True


def test_div7_1(input):
    #a = 12
    result = divisible.div7(input)
    assert result == False


def test_div9(input):
    #a = 18
    result = divisible.div9(input)
    assert result == True


def test_div9_1(input):
    #a = 12
    result = divisible.div9(input)
    assert result == False


def test_div11(input):
    #a = 22
    result = divisible.div11(input)
    assert result == True


def test_div11_1(input):
    #a = 12
    result = divisible.div11(input)
    assert result == False