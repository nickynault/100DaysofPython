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

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
turn1 = input("You\'re at a crossroads. Do you want to go left or right?\n").lower()
if turn1 == "left":
    turn2 = input(
        "You've come to the lake. There is an island in the middle of the lake. Do you want to wait or to swim across?\n").lower()
    if turn2 == "wait":
        turn3 = input(
            "You ride a boat across, eventually, and reach the house. There are... 3 front doors? Which do you choose to enter: Red, Blue or Yellow?\n").lower()
        if turn3 == "yellow":
            print(
                "Behind the yellow door is a small room filled with teeming chests of gold. You've found it! You've won!")
        elif turn3 == "blue":
            print("Behind the door is a pack of bloodthirsty badgers. You are eviscerated. Game Over.")
        elif turn3 == "red":
            print(
                "As you creak open the door, a raging fire explodes with its newfound oxygen fueled rage. You are char-broiled. Game Over.")
        else:
            print("Game Over.")
    else:
        print("You were attacked by a myriad of trout and drowned. Game Over.")
else:
    print("You fell into a hole. Game Over.")
