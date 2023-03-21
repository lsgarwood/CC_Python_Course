# Control Flow

# Booolean Expression
# If an expression is true or false

# Relational Operators
# Equals =
# Not equals !=
# These operators compare two items and return True or False if they are equal or not.

1 == 1     # True
 
2 != 4     # True
 
3 == 5     # False
 
'7' == 7   # False

# Boolean Variables
# Boolean variables can be created in several ways. The easiest way is to simply assign True or False to a variable:

set_to_true = True
set_to_false = False

# You can also set a variable equal to a boolean expression.

bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

# These variables now contain boolean values, so when you reference them they will only return the True or False values of the expression they were assigned.

print(bool_one)    # True
print(bool_two)    # False
print(bool_three)  # True

my_baby_bool = "true"
print(type(my_baby_bool))
# Output: <class 'str'>
my_baby_bool_two = True
print(type(my_baby_bool_two))
# Output: <class 'bool'>

# If statements
is_raining = True
if is_raining:
  print("bring an umbrella")
# Output: bring an umbrella

user_name = "Lauren"
if user_name == "Dave":
  print("Get off my computer Dave!")
# Output: Get off my computer Dave!

user_name = "angela_catlady_87"
if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")
  # Output: I know it is you, Dave! Go away!

# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to

age = 8
if age <= 13:
  print("Sorry, parental control required")

# exercise
x = 20
y = 20

# Write the first if statement here:
if x == y:
  print("These numbers are the same")

credits = 120

# Write the second if statement here:
if credits >= 120:
  print("You have enough credits to graduate!")

# Boolean operators: and
# and combines two boolean expressions and evaluates as True if both its components are True, but False otherwise.

(1 + 1 == 2) and (2 + 2 == 4)   # True
 
(1 > 9) and (5 != 6)            # False
 
(1 + 1 == 2) and (2 < 1)        # False
 
(0 == 10) and (1 + 1 == 1)      # False

# Excercise
(2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_one = False
(4 * 2 <= 8) and (7 - 1 == 6)
statement_two = True
credits = 120
gpa = 3.4

if credits >= 120:
  print("You meet the requirements to graduate!")

  if (credits >= 120) and (gpa >= 2.0):
    print("You meet the requirements to graduate!")

# Boolean Operators: or
# Notice that each or statement that has at least one True component is True, but the final statement has two False components, so it is False.
True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False

# Exercise
(2 - 1 > 3) or (-5 * 2 == -10)
statement_one = True
(9 + 5 <= 15) or (7 != 4 + 3)
statement_two = True
credits = 118
gpa = 2.0

if (credits >= 120) or (gpa >= 2.0):
  print("You have met at least one of the requirements.")

# Boolean Operator: not
# This operator is straightforward: when applied to any boolean expression it reverses the boolean value. So if we have a True statement and apply a not operator we get a False statement.
not 1 + 1 == 2  # False
not 7 < 0       # True

#Exercise
not (4 + 5 <= 9)
statement_one = False
not (8 * 2) != 20 - 4
statement_two = True

credits = 120
gpa = 1.8

if (not credits >= 120):
  print("You do not have enough credits to graduate.")

if (not gpa >= 2.0):
  print("Your GPA is not high enough to graduate.")

if (not credits >= 120) and (not gpa >= 2.0):
  print("You do not meet either requirement to graduate!")

# Else Statements
# else statements allow us to elegantly describe what we want our code to do when certain conditions are not met.
# else statements always appear in conjunction with if statements.

weekday = True
if weekday:
  print("wake up at 6:30")
else:
  print("sleep in")

# Or
if age >= 13:
  print("Access granted.")
else:
  print("Sorry, you must be 13 or older to watch this movie.")

# Exercise
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")


# Else if
donation = 350
print("Thank you for the donation!")
 
if donation >= 1000:
  print("You've achieved platinum status")
elif donation >= 500:
  print("You've achieved gold donor status")
elif donation >= 100:
  print("You've achieved silver donor status")
else:
  print("You've achieved bronze donor status")

# Exercise
grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")

# Review
# Boolean expressions are statements that can be either True or False
# A boolean variable is a variable that is set to either True or False.
# We can create boolean expressions using relational operators:
# ==: Equals
# !=: Not equals
# >: Greater than
# >=: Greater than or equal to
# <: Less than
# <=: Less than or equal to
# if statements can be used to create control flow in your code.
# else statements can be used to execute code when the conditions of an if statement are not met.
# elif statements can be used to build additional checks into your if statements

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
if planet > 6:
  print("Please enter a planet 1-6")
else:
  if planet == 1:
    weigth = weight * 0.91
  elif planet == 2:
    weight = weight * 0.38
  elif planet == 3:
    weight = weight * 2.34
  elif planet == 4:
    weight = weight * 1.06
  elif planet == 5:
    weight = weight * 0.92
  elif planet == 6:
    weight = weight * 1.19
  print("Your weight: ", weight)

  # Magic 8-Ball
  import random

name = "Lauren"
question = "Will I meet a prince?"
answer = ""
random_number = random.randint(1,10)

# print(random_number)

if (random_number == 1):
  answer += "Yes - definitely"
elif (random_number == 2):
  answer += "It is decidedly so"
elif (random_number == 3):
  answer += "Without a doubt"
elif (random_number == 4):
  answer += "Reply hazy - try again"
elif (random_number == 5):
  answer += "Ask again later"
elif (random_number == 6):
  answer += "Better not tell you now"
elif (random_number == 7):
  answer += "My sources say no"
elif (random_number == 8):
  answer += "Outlook not so good"
elif (random_number == 9):
  answer += "Very doubtful"
elif (random_number == 10):
  answer += "For sure"
else:
  print("Error")

if question == "":
  print("Please enter a question to get your answer!")
else:
  if name != "":
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)
  else:
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)

# Shipping costs
weight = 41.5
cost_ground = 0
cost_drone = 0
premium_ground = 125

# Ground shipping
if (weight <= 2):
  cost_ground += weight * 1.5 + 20
elif (weight > 2) and (weight <= 6):
  cost_ground += weight * 3 + 20
elif (weight > 6) and (weight <= 10):
  cost_ground += weight * 4 + 20
elif (weight > 10):
  cost_ground += weight * 4.75 + 20

print("Ground Shipping cost: £", cost_ground)
print("Flat Ground Shipping cost: £",  premium_ground)

# Drone shipping
if (weight <= 2):
  cost_drone += weight * 4.5
elif (weight > 2) and (weight <= 6):
  cost_drone += weight * 9
elif (weight > 6) and (weight <= 10):
  cost_drone += weight * 12
elif (weight > 10):
  cost_drone += weight * 14.25 
  
print("Drone shipping cost: £", cost_drone)

cheapest_cost = ""

if (cost_ground > cost_drone):
  cheapest_cost += "Drone"
elif (cost_ground < cost_drone):
  cheapest_cost += "Ground"
  
print(cheapest_cost, " shipping is your cheapest option")

# Syntax errors
# SyntaxError means there is something wrong with the way your program is written — punctuation that does not belong, a command where it is not expected, or a missing parenthesis can all trigger a SyntaxError

# A NameError is reported by the Python interpreter when it detects a variable that is unknown.
# This can occur if a variable is used before it has been assigned a value or if a variable name is spelled differently than the point at which it was defined. The Python interpreter will display the line of code where the NameError was detected and indicate which name is found that was not defined.

# A TypeError is reported by the Python interpreter when an operation is applied to a variable of an inappropriate type.
# This can occur in Python when one attempts to use an operator on something of the incorrect type.