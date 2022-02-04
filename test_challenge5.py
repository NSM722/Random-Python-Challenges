import test

from challenge5 import valid_pin

def test_valid_pin():
    assert valid_pin('    ') == False
    assert valid_pin('1a2b3c') == False
    assert valid_pin('1234') == True
    assert valid_pin('45135') == False
    assert valid_pin('89abc1') == False
    assert valid_pin("900876") == True
    assert valid_pin(" 4983") == False
    assert valid_pin('1a 5b2') == False