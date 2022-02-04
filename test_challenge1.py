import pytest

from challenge1 import sum_multiples_of_3_and_5

def test_sum_multiples_of_3_and_5():
    assert sum_multiples_of_3_and_5(1, 10) == 'The total sum of multiples of 3 and 5 between 1 and 10, not including 10 is: 23'
    assert sum_multiples_of_3_and_5(1,1000) == 'The total sum of multiples of 3 and 5 between 1 and 1000, not including 1000 is: 233168'
    assert sum_multiples_of_3_and_5(3, 30) == 'The total sum of multiples of 3 and 5 between 3 and 30, not including 30 is: 195'