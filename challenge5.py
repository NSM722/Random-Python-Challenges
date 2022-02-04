"""
Create a function to test if a string is a valid pin or not.
A valid pin has:
Exactly 4 or 6 characters.
Only numerical characters (0-9).
No whitespace.
"""
def valid_pin(string_as_pin):
    return ' ' not in string_as_pin and string_as_pin.isdecimal() and (len(string_as_pin) == 4 or len(string_as_pin) == 6)
    