# Loops

# for loops
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for game in sport_games:
  print(game)

# for loops with range()
promise = "I will finish the python loops module!"
for temp in range(5):
  print(promise)

# while loops
# while <conditional statement>:
#   <action>

count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1

# output
# 0
# 1
# 2
# 3

# indentation
while count <= 3:
   # Loop Body
   print(count)
   count += 1
   # Any other code at this level of indentation will
   # run on each iteration

# elegant loops
count = 0
while count <= 3: print(count); count += 1

