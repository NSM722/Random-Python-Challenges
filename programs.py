# Sorting without using a method
"""list2 = [60, 20, 91, 22, 4, 24, 2, 30, 28, 8, 12]
new_list = []
while list2:
    min_int = list[0]
    for i in list2:
        print(f'printing {i}')
        if i < min_int:
            min_int = i
    new_list.append(min_int)
    list2.remove(min_int)
print(new_list)"""

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

print(new_list)
#############################################################
sum = 0
num_count = int(input('How many numbers will you average? '))
for i in range(1, num_count + 1):
    next_number = int(input('Enter number # ' + str(i) + ': '))
    sum += next_number
average = sum / num_count
average = round(average, 2)
print(average)
#############################################################
# GUESSING GAME WITH A WHILE LOOP
#import the random module to get access to the randint method
import random
#random selection of numbers in the game
special_num = random.randint(1, 10)
#set user guess to zero since numbers counted randomly are between 1 and 10
user_guess = 0
#Maximum trying count is 3
guessing_limit = 3
#Keep a count of how many times the use has guessed a number
user_guess_count = 0

#set the condition for the while loop
while user_guess != special_num and user_guess_count != guessing_limit:
    #convert the input to an integer
    user_guess = int(input('Please pick any number: '))
    #keeping count of how many times the user has guessed
    user_guess_count += 1
    if user_guess < special_num:
        print('Low pick')
    if user_guess > special_num:
        print('High pick')
    if user_guess == special_num:
        print('You rock!')
        break
#This final print statement will occur when the user has overguessed!
else:
    print('Better luck next time!')
#####################################
# CALL A FUNCTION FROM ANOTHER FUNCTION/nested functions
def Square(X):
    return (X * X)

def SumofSquares(Array, n):
    Sum = 0
    for i in range(n):
        SquaredValue = Square(Array[i])
        Sum += SquaredValue
    return Sum

Array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
Total = SumofSquares(Array, n)
print(Total)

########################################
# Using print/debug statements/comments in a function for debugging purposes
def has_a_vowel(a_str):
    print("Starting...")
    for letter in a_str:
        print("Checking", letter)
        if letter in "aeiou":
            print(letter, "is a vowel, returning True")
            return True
        print(letter, "is not a vowel, returning False")
        return False
    print("Done!")

print(has_a_vowel("abba"))
print(has_a_vowel("brrrrrrr it's cold"))

#########################################
# String Format Method
origPrice = float(input('Enter the original price: $'))

discount = float(input('Enter discount percentage: '))

newPrice = (1 - discount/100)*origPrice

calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)

print(calculation)
################################################
# Use of Map
def square(data):
    return data * data


numbers = [2, 4, 6, 8]

print(list(map(square, numbers)))

print([square(data) for data in numbers])
##################################################
# Lambda
numbers = [2, 4, 6, 8]

new_numbers_list = (list(map(lambda i: i * 2, numbers)))

print(new_numbers_list)
###################################################
# USE str.join() TO JOIN A LIST OF INTEGERS INTO A STRING
ints = [1,2,3]
# Convert each integer to a string
string_ints = [str(int) for int in ints]

print(string_ints)

print(type(string_ints))

# Combine each string with a comma
string_ints = ",".join(string_ints)

print(string_ints)
####################################################
names = 'Rosemary Mbatha Fernandes'
names_list = names.split()
#print(names_list)
sign = ""
#print('Starting the loop: ')
for name in names_list:
    #print(name)
    sign += name[0]
    #print(sign)
print(sign)
#print('Loop is complete')
#print(type(sign))
####################################################
# File write method
word_list = ['Go', 'Fuck', 'Yourself', 'Karen']

int_file = open('test.txt', 'w')

int_file.write('\n'.join(word_list))

int_file.close()
#--------------
word_list = ['Go', 'Fuck', 'Yourself']

int_file = open('test.txt', 'w')

for word in word_list:
    int_file.write(word + '\n')

int_file.close()
#--------------
word_list = ['Life', 'is', 'a', 'mess']

int_file = open('test.txt', 'a')

for word in word_list:
    print(word, file=int_file)

int_file.close()
#---------------
load_list = []

with open('numbers_file.txt', 'r') as load_mode:
    for line in load_mode:
        load_list.append(int(line.strip()))

load_list.sort()
print(load_list)
######################################################
answers_sample_dic = {'1': 'A', '2': 'B', '3': 'C'}

students = {}
students['Max'] = {'1': 'B', '2': 'B', '3': 'C'}
students['Sara'] = {'1': 'C', '2': 'C', '3': 'C'}
students['Dora'] = {'1': 'A', '2': 'B', '3': 'C'}
#print(students)

for (student, answers) in students.items():
    grade = 0
    for (question, answer) in answers.items():
        if answer == answers_sample_dic[question]:
            grade += 1
    students[student]['grade'] = grade
#print(students)

for (student, answers) in students.items():
    print(student, ': ', answers['grade'], sep='', end='; ')
#######################################################
# Binary number reloaded
number = 215
divisor = 2
binary_num_list = []

while number >= 0:
    res = number % divisor
    binary_num_list.append(res)
    number = number // 2

#print(binary_num_list)
binary_num_list.reverse()
binary_num_list_as_str = ''

for i in binary_num_list:
    binary_num_list_as_str += str(i)
print(binary_num_list_as_str)
#######################################################
def names_to_apa(names):
    names = names.replace(', and ', ', ')
    print(names)
    names = names.split(', ')
    print(names)
    names = [name.split() for name in names]
    print(names)
    names = [name[-1]+', '+(''.join(initial[0]+'.' for initial in name[:-1])) for name in names]
    print(names)
    names = ', '.join(names[:-1])+', '+names[-1]
    return names

print(names_to_apa("First Last, David Joyner, and George Burdell"))
# Last, F., Joyner, D., Burdell, G.
#######################################################
class ExerciseSession:
    def __init__(self, exercise_name, exercise_intensity, duration):
        self.exercise = exercise_name
        self.intensity = exercise_intensity
        self.time_in_minutes = duration

    def calories_burned(self):
        if self.intensity == "Low":
            return 4 * self.time_in_minutes
        elif self.intensity == 'Medium':
            return 8 * self.time_in_minutes
        else:
            return 12 * self.time_in_minutes

    def get_exercise(self):
        return self.exercise

    def get_intensity(self):
        return self.intensity

    def get_duration(self):
        return self.time_in_minutes

    def set_exercise(self, new_exercise):
        self.exercise = new_exercise

    def set_intensity(self, new_intensity):
        self.intensity = new_intensity

    def set_duration(self, new_duration):
        self.time_in_minutes = new_duration


new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())
##########################################################
class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist


song_1 = Song("You Belong With Me", "Fearless", 2008, Artist("Taylor Swift", "Big Machine Records, LLC"))
song_2 = Song("All Too Well", "Red", 2012, song_1.artist)
song_3 = Song("Up We Go",  "Midnight Machines", 2016, Artist("LiGHTS", "Warner Bros. Records Inc."))


"""print(song_1.artist.name)
print(song_1.artist.label)
print(song_1.album)
print()
print(song_2.artist.name)
print(song_2.artist.label)
print(song_2.album)
print()
print(song_3.artist.name)
print(song_3.artist.label)
print(song_3.album)"""
###########################################################
class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last


class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []
###########################################################
# BUBBLE SORTING
def sort_with_bubbles(lst):
    swap_occurred = True
    while swap_occurred:
        swap_occurred = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                #So, if the items were 5 and 4, then:
                # - temp becomes 5 (lst[i])
                # - lst[i] becomes 4 (lst[i + 1])
                # - lst[i + 1] becomes 5 (temp)
                swap_occurred = True
    return lst


print(sort_with_bubbles([5, 3, 1, 2, 4]))
############################################################

def get_pets_string(owner):
    pets_list = []
    #f'{owner.name.first} {owner.name.last}\'s pets are: '
    for pet in owner.pets:
        pets_list.append(pet.name.first + ' ' + pet.name.last)
    return "{0} {1}'s pets are: {2}".format(owner.name.first, owner.name.last, ", ".join(pets_list))
owner_1 = Owner(Name("David", "Joyner"))
owner_2 = Owner(Name("Audrey", "Hepburn"))

pet_1 = Pet(Name("Boggle", "Joyner"), owner_1)
pet_2 = Pet(Name("Artemis", "Joyner"), owner_1)
pet_3 = Pet(Name("Pippin", "Hepburn"), owner_2)

owner_1.pets.append(pet_1)
owner_1.pets.append(pet_2)
owner_2.pets.append(pet_3)

print(get_pets_string(owner_1))
print(get_pets_string(owner_2))
############################################################
# Selection sorting
def sort_with_select(a_list):
    for i in range(len(a_list)):

        minIndex = i

        for j in range(i + 1, len(a_list)):

            # The loops above already take care of the overall
            # control flow of selection sort: all we need to do
            # here is see if the current item is lower than the
            # lowest-found item on the current iteration. So,
            # we check the current item against the lowest-found
            # item so far:
            if a_list[j] < a_list[minIndex]:
                # And if it's lower, we note that this is the new
                # lowest-found item:
                minIndex = j
        minValue = a_list[minIndex]
        del a_list[minIndex]
        a_list.insert(i, minValue)
    return a_list
print(sort_with_select([5, 3, 1, 2, 4]))
#############################################################
"""The mergeSort function shown in ActiveCode 1 begins by asking the base case question. 
If the length of the list is less than or equal to one, then we already have a sorted list and no more processing is necessary. 
If, on the other hand, the length is greater than one, then we use the Python slice operation to extract the left and right halves. 
It is important to note that the list may not have an even number of items. That does not matter, as the lengths will differ by at most one."""
def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

def mergesort(lst):
    if len(lst) <= 1:
        return lst
    else:
        midpoint = len(lst) // 2
        left = mergesort(lst[:midpoint])
        right = mergesort(lst[midpoint:])
        newlist = []
        while len(left) and len(right) > 0:
            if left[0] < right[0]:
                newlist.append(left[0])
                del left[0]
            else:
                newlist.append(right[0])
                del right[0]
        newlist.extend(left)
        newlist.extend(right)
        return newlist
print(mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))
##############################################################
# LINEARSEARCH
# First, we declare the function:
def linear_search(a_list, an_item):
    # Then, we iterate through the list:
    for i in range(len(a_list)):
        # If we've found the item, we're done! Go ahead and
        # return this index.
        if a_list[i] == an_item:
            return i
    # If we reach the end of the function it means we never
    # returned an index, which means we never found the item
    # and can return False.
    return False
a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear_search(a_list, 6))
##############################################################
# Collatz Conjecture
"""The Collatz conjecture describes a sequence: starting with a positive number, 
if the number if even, halve it. If the number is odd, triple it and then add 1. 
Repeat. This sequence will always eventually reach 1 and should then stop. 
For example, if we started with 17:
17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1"""
def collatz(current_number):
    print(current_number)
    if current_number % 2 == 0:
        return collatz(current_number // 2)
    else:
        if current_number != 1:
            return collatz(current_number * 3 + 1)
        else:
            pass

def collatz(current_number):
    print(current_number)
    if current_number % 2 == 0:
        return collatz(current_number // 2)
    elif current_number % 2 == 1:
        return collatz(current_number * 3 - 1)
    else:
        pass
###############################################################
# Names class
class Name():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def find_printed_name(self):
        return f'{self.first_name} {self.last_name}'

    def find_sortable_name(self):
        return f'{self.last_name}, {self.first_name[0]}'
test_name = Name("David", "Joyner")
print(test_name.first_name)
print(test_name.last_name)
print(test_name.find_printed_name())
print(test_name.find_sortable_name())
################################################################
# Counting capital consonants
def count_capital_consonants (string):
    count = 0
    for char in string:
        if char not in "AEIOU":
            if 'A' < char < 'Z':
                count += 1
    return count
################################################################
# Anagram checker
def are_anagrams(string1, string2):
    #convert all characters to lower case
    string1 = string1.lower()
    #Get rid of the spaces
    string1 = string1.replace(' ', '')
    #print('printing', string1)
    # convert all characters to lower case
    string2 = string2.lower()
    # Get rid of the spaces
    string2 = string2.replace(' ', '')
    #print('printing', string2)
    if len(string1) == len(string2):
        if sorted(string1) == sorted(string2):
            return True
        return False
    return False
#option 2
def are_anagrams(first_word, second_word):
    first_word = first_word.lower()
    second_word = second_word.lower()
    first_word = first_word.replace(' ', '')
    second_word = second_word.replace(' ', '')
    letters = []
    for char in first_word:
        letters.append(char)
    for char in second_word:
        if char not in letters:
            return False
        letters.remove(char)
        print(letters)
    return len(letters) == 0
##################################################################
# Binary date search
from datetime import date
def binary_search_year(dates_lookup_list, year_to_search):
    dates_lookup_list.sort()
    #print(dates_lookup_list)
    if len(dates_lookup_list) == 0:
        return False
    middle = len(dates_lookup_list) // 2
    if dates_lookup_list[middle].year == year_to_search:
        return True
    elif year_to_search < dates_lookup_list[middle].year:
        return binary_search_year(dates_lookup_list[:middle], year_to_search)
    else:
        return binary_search_year(dates_lookup_list[middle + 1:], year_to_search)
# Recursive_binary_search
"""We assume the list in this program is already sorted"""
def recursive_binary_search(a_list, target):
    #checking whether the list is empty
    if len(a_list) == 0:
        return False
    else:
        list_midpoint = len(a_list) // 2
        if a_list[list_midpoint] == target:
            return True
        else:
            if a_list[list_midpoint] < target:
                return recursive_binary_search(a_list[list_midpoint + 1:], target)
            else:
                return recursive_binary_search(a_list[:list_midpoint], target)
##################################################################
# Stack class

class Stack:
    def __init__(self):
        self.list = []

    def stack_push(self, add_to_list):
        return self.list.append(add_to_list)

    def stack_pop(self):
        if len(self.list) == 0:
            return None
        #Then, we need to do three things: first we need to
        #save the last item to return. Then we need to remove
        #it from the list. Then we need to actually return it.
        #Notice that these have to be done in this order: if we
        #delete it first, we don't know what it was and can't
        #return it. If we return before deleting, then the function
        #is over and the list is unchanged.
        item = self.list[-1]
        del self.list[-1]
        return item
##################################################################
# Queue class
class Queue:
    def __init__(self):
        self.queue_list = []

    def enqueue(self, add_to_queue):
        self.queue_list.insert(0, add_to_queue)
        #self.queue_list.append(add_to_queue)

    def dequeue(self):
        return self.queue_list.pop()
        #if len(self.items) == 0:
        #    return None
        #item = self.items[0]
        #del self.items[0]
        #return item
##################################################################
# Binary tree search
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_search(single_node, value):
    if single_node:
        if single_node.value == value:
            return True
        elif single_node.value < value:
            return binary_tree_search(single_node.right, value)
        return binary_tree_search(single_node.left, value)
    return False
##################################################################
# ObjectstoDictionaries
class Nation:
    def __init__(self, short_name, long_name, iso_code, iso_short, iso_long, capital):
        self.short_name = short_name
        self.long_name = long_name
        self.iso_code = iso_code
        self.iso_short = iso_short
        self.iso_long = iso_long
        self.capital = capital

def to_dictionaries(data_input):
    data_dict = {}
    for data in data_input:
        if data.short_name not in data_dict.keys():
            data_dict[data.short_name] = {}
            data_dict[data.short_name]['long_name'] = data.long_name
            data_dict[data.short_name]['iso_code'] = data.iso_code
            data_dict[data.short_name]['iso_short'] = data.iso_short
            data_dict[data.short_name]['iso_long'] = data.iso_long
            data_dict[data.short_name]['capital'] = data.capital
        #   data_dict[data.short_name] = {data.long_name, data.iso_code, data.iso_short, data.iso_long, data.capital}
        else:
            pass
    return data_dict
###################################################################
# Linked list search
class LinkedListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node


def linked_list_search(node, search):
    # If this node's value is the one we're searching for,
    # we're done! Return True.
    if node.value == search:
        return True
    # Otherwise, we need to check if the next node is None.
    # If it is, we've reached the end of the list without
    # finding our search term, so we return False:
    elif node.next_node == None:
        return False
    # Then, if this node doesn't have the value we're looking
    # for, and if this node isn't the last node, then we call
    # linked_list_search on the next node:
    else:
        return linked_list_search(node.next_node, search)

#https://www.koderdojo.com/blog/linear-search-of-linked-list
"""def linked_list_search(node, term):
    current_node = node
    while current_node != None:
        if current_node.value == term:
            return True
        current_node = current_node.next_node
    return False"""
#################################################################
# Name generator
def generate_name(filename, names):
    fictional_names =[]
    print_output = open(filename, 'r')
    split_names = names.split(" ")
    line_to_read = [ord(split_names[0][0])-65, ord(split_names[1][0])-65+26]
    for position, name in enumerate(print_output):
        if position in line_to_read:
            name=name.replace("\n", "")
            fictional_names.append(name)
    return fictional_names[0]+" "+fictional_names[1]
################################################################
# Least common multiple
def find_lcm(int1, int2):
    if int1 > int2:
        large_int = int1
    else:
        large_int = int2

    while(True):
        if ((large_int % int1 == 0) and (large_int % int2 == 0)):
            lcm = large_int
            break
        large_int += 1

    return lcm
################################################################

"""names_file = open('test2.txt', 'r')

chars = names_file.readlines()
for char in chars:
    split_chars = char.split(',')
    print(split_chars)
    int_chars = []
    for i in split_chars:
        if i.isalnum():
            int_chars.append(i)
        print(int_chars)"""
#################################################################
def check_winner(tup_list):
    for i in tup_list:
        if len(i) == 6:
            return f'Player {tup_list.index(i)} wins!'
        return 'Keep Playing!'


winning_player = ["Red", "Orange", "Yellow", "Purple", "Green", "Blue"]
losing_player_a = []
losing_player_b = ["Red", "Orange"]
losing_player_c = ["Yellow", "Purple", "Green", "Blue"]

print(check_winner((winning_player, losing_player_a, losing_player_b)))
print(check_winner((losing_player_a, losing_player_b, losing_player_c)))
print(check_winner((losing_player_b, losing_player_c, winning_player)))
######################################################################
# Binary serach O notation
def binary_search(n):     # binary search big O notation is similar to log 2 n or 2 raised to the power of 'x' times yields n_times
    # the complexity of the Algorithm is always 1 plus O(log n)
    num_of_operations = 1
    # the base or exponent is always 2
    exponent = 2
    if n > 1:
    # checking that n is bigger than 1
        while n // exponent:
            num_of_operations += 1
            n = n // exponent
        #print(n) #further visualize the value of n changing
        #adjust the value of n since you earlier divide it by 2
        return num_of_operations
    return 1
#######################################################################
