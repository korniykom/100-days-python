
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

firstChoice = input("left or right")
if(firstChoice == "left"):
    secondChoice = input("swim or sink")
    if(secondChoice == "swim"):
        thirdChoice = input("1 2 or 3")
        if(thirdChoice == "1"):
            print("You won!")
        else:
            print("Game over")
    else:
        print("Game over")

else:
    print("Game over")

