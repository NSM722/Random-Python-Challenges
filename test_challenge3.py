import pytest

from challenge3 import isPalindrome

def test_isPalindrome():
    assert isPalindrome('MADAM') 
    assert isPalindrome(48984) 
    assert isPalindrome(191) 
    assert isPalindrome('BOB')

