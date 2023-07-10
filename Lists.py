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