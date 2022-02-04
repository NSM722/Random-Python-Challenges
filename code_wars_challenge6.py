"""Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order."""

def digitize(n):
    #reverse_number = 0
    reverse_n_list = []
    if n == 0:
        return [0]
    else:
        while n != 0:
            digit = n % 10
            reverse_n_list.append(digit)
            #reverse_number *= 10
            #reverse_number += digit
            n //= 10
    return reverse_n_list
