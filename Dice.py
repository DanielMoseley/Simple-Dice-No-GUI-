from random import randint
import sys

minimum = 1
while True:
    try:
        maximum = int(input("How many sides does the dice have?: "))
    except ValueError:
        print("Please Enter an integer: ")
    else:
        break

roll_dice_str = input("Do you want to roll the dice? [y/n] :")
roll_dice = roll_dice_str.lower() in ("y", "yes")

while roll_dice == True:
    Random_Number = randint(minimum,maximum)
    print(str(Random_Number))
    roll_dice_str = input("Do you want to roll the dice? [y/n] :")
    roll_dice = roll_dice_str.lower() in ("y", "yes")
else:
    sys.exit()
