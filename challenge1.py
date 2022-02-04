"""
If we list all the numbers between 1 and 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
Add those numbers together and you get 23.
Find the sum of all the numbers between 1 and 1000 that are multiples of 3 or 5. 
"""
def sum_multiples_of_3_and_5(start_num, end_num):
    total_sum = 0
    for i in range(start_num, end_num):
        if i % 3 == 0 or i % 5 == 0:
            #print(i, end=" ")
            total_sum += i
    return f'The total sum of multiples of 3 and 5 between {start_num} and {end_num}, not including {end_num} is: {total_sum}'
