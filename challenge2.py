"""
Tip calculator
Create a Tip calculator (or rather a function for a tip calculator)!
For any number of guests sharing a restaurant bill, calculate how much tip each guest needs to pay. 
Use variables to store the number of guests, the amount of the bill and the tip in percentage, e.g. 
guest = 2;
bill = 80;
tipPercentage = 10;
Create a function which takes these values as input and outputs the total amount each guest needs to pay as well as the amount of tip that is included, 
eg `Each guest needs to pay: 44 euro` and `The amount of tip for each guest is: 4 euro`.
"""
def tip_calculator(guest, bill, tip_percentage):
    bill_per_guest = bill // guest
    tip_percentage /= 100
    tip_per_guest = (bill * tip_percentage) // guest
    total_bill_per_guest = bill_per_guest + tip_per_guest
    return f'Each guest needs to pay: {round(total_bill_per_guest)} euro and The amount of tip for each guest is: {round(tip_per_guest)} euro'
