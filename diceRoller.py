import random
# now we need to simulate a 2 dice roller program

roll_dice = input("Would you like to roll the dice?: ").lower()

while roll_dice:
    if roll_dice == "yes":
        side_1 = random.choice(range(1, 7))
        side_2 = random.choice(range(1, 7))
        dice_sum = side_1 + side_2

        print(str(side_1) + " and " + str(side_2))
        print("you rolled a " + str(dice_sum))

        roll_again = input("would you like to roll again?: ").lower()
        if roll_again != "yes":
            print("Thank you for playing.")
            break
    else:
        print("Thank you for playing.")
        break

print("Have a nice day!")