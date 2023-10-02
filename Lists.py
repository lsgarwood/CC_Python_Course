# List Methods

append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')
 
print(append_example)
# will output: ['This', 'is', 'an', 'example', 'list']

# List: Plus (+) - list concatenation
items_sold = ["cake", "cookie", "bread"]
items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)
# output: ['cake', 'cookie', 'bread', 'biscuit', 'tart']

# We can only use + with other lists
my_list = [1, 2, 3]
my_list + 4 # gives an error: TypeError: can only concatenate list (not "int") to list

# If we want to add a single element using +, we have to put it into a list with brackets ([]):
my_list + [4]

# Accessing elements of list
calls = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]
print(calls[2]) # output: Amare
# Note: When accessing elements of a list, you must use an int as the index. If you use a float, you will get an error. This can be especially tricky when using division. For example print(calls[4/2]) will result in an error, because 4/2 gets evaluated to the float 2.0.
# To solve this problem, you can force the result of your division to be an int by using the int() function. int() takes a number and cuts off the decimal point. For example, int(5.9) and int(5.0) will both become 5. Therefore, calls[int(4/2)] will result in the same value as calls[2], whereas calls[4/2] will result in an error.

# Accessing list elements negative
pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]
print(pancake_recipe[-1]) # output: love
# We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(index5_element) # cereal
print(last_element) # cereal

# Modifying list elements
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
garden[2] = "Strawberries"
print(garden) # output: ["Tomatoes", "Green Beans", "Strawberries", "Grapes"]
# negative indices work too:
garden[-1] = "Raspberries"
print(garden) # output: ["Tomatoes", "Green Beans", "Strawberries", "Raspberries"]

# Shrinking a list - remove
shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]
shopping_line.remove("Chris")
print(shopping_line) # output: ["Cole", "Kip", "Sylvana"]

# We can also use .remove() on a list that has duplicate elements - Only the first instance of the matching element is removed:
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
shopping_line.remove("Chris")
print(shopping_line) # ["Cole", "Kip", "Sylvana", "Chris"]

# Two Dimensional Lists
# We’ve seen that the items in a list can be numbers or strings. Lists can contain other lists! We will commonly refer to these as two-dimensional (2D) lists

heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]

#A 2d list with three lists in each of the indices. 
tic_tac_toe = [
            ["X","O","X"], 
            ["O","X","O"], 
            ["O","O","X"]
]

# append to 2d list
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]
heights.append(["Vik", 68])

# Accessing a 2d list
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]
#Access the sublist at index 0, and then access the 1st index of that sublist. 
noelles_height = heights[0][1] 
print(noelles_height) # output: 61
# exercises
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)
# access ellies score using negative indices
ellies_score = class_name_test[-1][-1]
print(ellies_score)

# Modifying 2d lists
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
# "Jenny" changed their mind and is now more interested in "Meditation"
# To change a value in a two-dimensional list, reassign the value using the specific index
# The list of Jenny is at index 0. The hobby is at index 1. 
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies) # output = [["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

# create 2d list
incoming_class = [["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]
print(incoming_class)
# modify madisons grade - positive index
incoming_class[2][2] = 8
print(incoming_class)
# modify kennys name - negative index
incoming_class[-3][-3] = "Ken"
print(incoming_class)

# Review
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
# add a size for depak
preferred_size.append("Medium")
print(preferred_size)
# create new list
customer_data = [["Ainsley","Small",True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)
# change chanis shipping
customer_data[2][2] = False
print(customer_data)
# remove bens shipping
customer_data[1].remove(False)
print(customer_data)
# add more customer data to new list
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

# Gradebook Exercise
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# create combined list
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# append new list
gradebook.append(["computer science", 100])
# append another list
gradebook.append(["visual arts", 93])
# modify last grade
gradebook[-1][-1] = gradebook[-1][-1] + 5
# remove poetry grade
gradebook[2].remove(85)
# append a pass to poetry calss
gradebook[2].append("Pass")
print(gradebook)

# combine two gradebook lists
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

# Adding by Index: Insert
# Some important things to note:
# The order and number of the inputs is important. 
# The .insert() method expects two inputs, the first being a numerical index, followed by any value as the second input.
# When we insert an element into a list, all elements from the specified index and up to the last index are shifted one index to the right. 
# This does not apply to inserting an element to the very end of a list as it will simply add an additional index and no other elements will need to shift.

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)
# insert pineapple
front_display_list.insert(0, "Pineapple")
print(front_display_list)

# Removing by Index: Pop

# The .pop() method takes an optional single input:
# The index for the element you want to remove
# The method can be called without a specific index. Using .pop() without an index will remove whatever the last element of the list is. In our case "Clowns 101" gets removed.
# The method can be called with an optional specific index to remove
# We don’t have to save the removed value to any variable if we don’t care to use it late

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# remove python
data_science_topics.pop()
print(data_science_topics)
# remove algorithms
data_science_topics.pop(3)
print(data_science_topics)

# consecutive lists: Range
# The range() function is unique in that it creates a range object
# In order to use this object as a list, we have to first convert it using another built-in function called list().
# The list() function takes in a single input for the object you want to convert

#list 0 to 8
number_list = range(9)
print(list(number_list))
#list 0 to 7
zero_to_seven = range(8)
print(list(zero_to_seven))

# By default, range() creates a list starting at 0. However, if we call range() with two inputs, we can create a list that starts at a different number
my_list = range(2, 9)
print(list(my_list)) # output [2, 3, 4, 5, 6, 7, 8]

# If we use a third input, we can create a list that “skips” numbers.
# range(2, 9, 2) will give us a list where each number is 2 greater than the previous number:

my_range2 = range(2, 9, 2)
print(list(my_range2)) # output [2, 4, 6, 8]

# Length
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 100)

# length of long_list
long_list_len = len(long_list)
print(long_list_len)
# length of big_range
big_range_length = len(big_range)
print(big_range_length)

# Slicing Lists 1
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
# slice first two elements
beginning = suitcase[0:2]
print(beginning)
# make new slice, and print
middle = suitcase[2:4]
print(middle)

# Slicing Lists 2
# If we want to select the first n elements of a list, we could use: list[:n]
fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
fruits[:3] # output ['apple', 'cherry', 'pineapple']

# We can do something similar when we want to slice the last n elements in a list
print(fruits[-2:]) # output ['orange', 'mango']

# Negative indices can also accomplish taking all but n last elements of a list
fruits[:-1] # output ['apple', 'cherry', 'pineapple', 'orange']

# exercise
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"] 
# last two elements
last_two_elements = suitcase[-2:]
print(last_two_elements)
# all but last three elements
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

# Counting in a list
letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
# If we want to know how many times i appears in this word, we can use the list method called .count()
num_i = letters.count("i")
print(num_i) # output 4

# Notice that since .count() returns a value, we can assign it to a variable to use it.
# We can even use .count() to count element appearances in a two-dimensional list
number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]] 
# how often [100, 200] appears
num_pairs = number_collection.count([100, 200])
print(num_pairs) # output 2

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]
# how many votes for jake
jake_votes = votes.count("Jake")
print(jake_votes) # output 9
 
# Sorting Lists 1
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort()
print(names) # output ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
# As we can see, the .sort() method sorted our list of names in alphabetical order
# .sort() also provides us the option to go in reverse
names.sort(reverse=True)
print(names) # output ['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']

# Note: The .sort() method does not return any value and thus does not need to be assigned to a variable since it modifies the list directly. 
# If we do assign the result of the method, it would assign the value of None to the variable

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)
# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
cities.sort(reverse=True)
print(cities)

# Sorting Lists 2
# The sorted() function is different from the .sort() method in two ways:
# It comes before a list, instead of after as all built-in functions do.
# It generates a new list rather than modifying the one that already exists

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
# create a new list, called sorted_names
sorted_names = sorted(names)
print(sorted_names) # output ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
# note that using sorted did not change names

# Review
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]
# how many items in warehouse len()
inventory_len = len(inventory)
# select first element
first = inventory[0]
# select last element
last = inventory[-1]
# select items in the inventory - index 2, upto not incl. 6
inventory_2_6 = inventory[2:6]
# first three items
first_3 = inventory[:3]
# how many twin beds?
twin_beds = inventory.count("twin bed")
# remove 5th element
removed_item = inventory.pop(4)
# insert at 11th
inventory.insert(10, "19th Century Bed Frame")
# sort inventory
inventory.sort() 
# or
inventory = sorted(inventory)

# Pizza exercise
# toppings list
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies","mushrooms"]
# prices list
prices = [2, 6, 1, 3, 2, 7, 2]
# how many $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
# length of toppings list
num_pizzas = len(toppings)
# print
print(f"We sell {num_pizzas} different kinds of pizza!")
# new 2d list
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
# print
print(pizza_and_prices)
# sort into ascending price
pizza_and_prices.sort()
print(pizza_and_prices)
# store first element
cheapest_pizza = pizza_and_prices[0]
# most expensive
priciest_pizza = pizza_and_prices[-1]
# remove anchovies
pizza_and_prices.pop()
# add peppers
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)
# three cheapest
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)