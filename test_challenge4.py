import pytest

from challenge4 import covid19_hand_wash_timer

def test_covid19_hand_wash_timer():
    assert covid19_hand_wash_timer(8, 7) == '588 minutes and 0 seconds'
    assert covid19_hand_wash_timer(0, 0) == '0 minutes and 0 seconds'
    assert covid19_hand_wash_timer(7, 9) == '661 minutes and 30 seconds'

