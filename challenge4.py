"""Wash Your Hands :)
It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.
Create a function that takes the number of times a person washes their hands per day 
N and the number of months they follow this routine nM and calculates the duration 
in minutes and seconds that person spends washing their hands."""

def covid19_hand_wash_timer(wash_per_day, total_months):
    days_in_a_month = 30
    hand_wash_in_seconds = 21
    hour_in_minutes = 60
    total_months_of_hand_wash_in_days = total_months * days_in_a_month
    hand_wash_count_per_day_in_seconds = wash_per_day * hand_wash_in_seconds
    total_time_count_in_minutes = (total_months_of_hand_wash_in_days * hand_wash_count_per_day_in_seconds) // hour_in_minutes
    total_time_count_in_seconds = (total_months_of_hand_wash_in_days * hand_wash_count_per_day_in_seconds) % hour_in_minutes
    return f'{total_time_count_in_minutes} minutes and {total_time_count_in_seconds} seconds'
