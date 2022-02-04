"""
Palindrome Checker
A palindrome is a number/string that is same forwards and backwards. 
For example 545, 151, 34543, 343, 171, 48984 are palindrome. A string like LOL, MADAM are also palindromes. 
Write a function called isPalindrome that takes an variable and returns true or false if the variable 
is a palindrome.
"""
def isPalindrome(test_input):
    if type(test_input) == str:
        return (test_input) == test_input[::-1]
    elif type(test_input) == int:
        reverse_test_input = 0
        while test_input != 0:
            remainder = 0
            remainder %= 10
            reverse_test_input *= 10
            reverse_test_input += remainder
            test_input //= 10
        return test_input == reverse_test_input
    pass

