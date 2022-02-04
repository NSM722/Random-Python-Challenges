import pytest

from challenge2 import tip_calculator

def test_tip_calculator():
    assert tip_calculator(2, 80, 10) == 'Each guest needs to pay: 44 euro and The amount of tip for each guest is: 4 euro'
    assert tip_calculator(4, 400, 7) == 'Each guest needs to pay: 107 euro and The amount of tip for each guest is: 7 euro'
    assert tip_calculator(3, 1545, 10) == 'Each guest needs to pay: 566 euro and The amount of tip for each guest is: 51 euro'

