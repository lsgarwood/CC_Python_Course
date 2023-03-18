# Hello World
my_name = "Lauren"
print("Hello and welcome " + my_name + "!")

# Comments
# Provide context for why something is written the way it is:
# This variable will be used to count the number of times anyone tweets the word persnickety
persnickety_count = 0

# Help other people reading the code understand it faster:
# This code will calculate the likelihood that it will rain tomorrow
complicated_rain_calculation_for_tomorrow()

# Ignore a line of code and see how a program will run without it:
# useful_value = old_sloppy_code()
useful_value = new_clean_code()

# Print
# The print() function is used to tell a computer to talk
print("Hello world!")

# a string is either surrounded by double quotes ("Hello world") or single quotes ('Hello world'). It doesn’t matter which kind you use, just be consistent.
print("Lauren")
print('Lauren')

# Variables
# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "Porridge"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner
meal = "Lamb Chops"

# Printing out dinner
print("Dinner:")
print(meal)

# Errors
# Two common errors that we encounter while writing Python are SyntaxError and NameError.
# SyntaxError means there is something wrong with the way your program is written — punctuation that does not belong, a command where it is not expected, or a missing parenthesis can all trigger a SyntaxError.
# A NameError occurs when the Python interpreter sees a word it does not recognize. Code that contains something that looks like a variable but was never defined will throw a NameError.

# Numbers
# An integer or int is a whole number
# A floating-point or float is a decimal number
# Can be assigned to variables sor used literally
an_int = 2
a_float = 2.1
 
print(an_int + 3)
# Output: 5

# Calculations
# Python performs the arithmetic operations of addition, subtraction, multiplication, and division with +, -, *, and /.
# New versions of Python converts all ints to floats before performing division
# Division can throw its own special error: ZeroDivisionError. Python will raise this error when attempting to divide by 0.

# Changing Numbers
# Variables that are assigned numeric values can be treated the same as the numbers themselves.
coffee_price = 1.50
number_of_coffees = 4
# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)
 
# Updating the price 
coffee_price = 2.00
 
# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

# define variables for quilt
quilt_width = 8
quilt_length = 12

#multiply variables to calculate squares required
print(quilt_width * quilt_length)
# update variable
quilt_length = 8
# now do same calucilation
print(quilt_width * quilt_length)
# will give an updated amount

# Exponents
# 2 to the 10th power, or 1024
print(2 ** 10)
 
# 8 squared, or 64
print(8 ** 2)
 
# 9 * 9 * 9, 9 cubed, or 729
print(9 ** 3)
 
# We can even perform fractional exponents
# 4 to the half power, or 2
print(4 ** 0.5)

# Calculation of squares for:
# 6x6 quilt
print (6 * 6)
# 7x7 quilt
print (7 * 7)
# 8x8 quilt
print (8 * 8)
# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6 ** 4)

# Modulo
# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
 
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)

# concatenation
# The + operator doesn’t just add two numbers, it can also “add” two strings! The process of combining two strings is called string concatenation
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text
 
# Prints "Hey there!How are you doing?"
print(full_text)

full_text = greeting_text + " " + question_text
 
# Prints "Hey there! How are you doing?"
print(full_text)

# If you want to concatenate a string with a number you will need to make the number a string first, using the str() function. If you’re trying to print() a numeric variable you can use commas to pass it as a different argument rather than converting it to a string.
birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
 
# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2
 
# Prints "I am 10 years old today!"
print(full_birthday_string)
 
# If we just want to print an integer 
# we can pass a variable as an argument to 
# print() regardless of whether 
# it is a string.
 
# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6

print(message)

# Plus equals
# First we have a variable with a number saved
number_of_miles_hiked = 12
 
# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2
 
# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14

#The plus-equals operator also can be used for string concatenation, like so:
hike_caption = "What an amazing time to walk through nature!"
 
# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"

# Muiltiline strings
# By using three quote-marks (""" or ''') instead of one, we tell the program that the string doesn’t end until the next triple-quote. This method is useful if the string being defined contains a lot of quotation marks and we want to be sure we don’t close it prematurely.

leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""
# In the above example, we assign a famous poet’s words to a variable. Even though the quote contains multiple linebreaks, the code works!
# If a multi-line string isn’t assigned a variable or used in an expression it is treated as a comment.

# Assign the string here
to_you = """ Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
"""
print(to_you)

# Review Exercse - Receipt Production
lovely_loveseat_description = """
Lovely LOveseat. Tufted polyester blend on wood. 32 inches. Red or white
"""

lovely_loveseat_price = 254.00

stylish_settee_description = """"
Stylish setee. Faux leather on birch. 29.50 inches. Black
"""

stylsih_settee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown
"""

luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)