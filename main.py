print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("")

cross = input("You're standing at a cross road, which direction should you go?\n 'left' or 'right'?\n ").lower()
print("")

if cross == "left":
  lake = input('''You've come into a lake. There's an island in the middle of the lake.
    Type "wait" to wait for boat. Or type "swim to swim across"? 
    ''' ).lower()

  print("")
  if lake == "wait":
    # continue
    doors = input('''You made it to the island unharmed.
    There is a house with 3 doors. One red, One yellow, and One blue.
    Which door do u choose? (red, yellow, or blue)?
    ''').lower()

    print("")
    if doors == "red":
      print("You've stepped inside a room full of snakes! Game Over!")
    elif doors == "yellow":
      print("You found the treasure! Congratulations!")
    elif doors == "blue":
      print("You've open a door and the room was empty. Game Over!")
  else: 
    print("You got attacked by an angry trout. Game Over!")
else:
  print("You fell into a hole. Game Over!")
