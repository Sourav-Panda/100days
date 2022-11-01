direction = input("Welcome toTreasure Island. Find the Treasure. \n Do you want to go left or right " )
direction = direction.lower()
if direction == "left" or direction =="l":
    a = input("swim or wait ")
    a = a.lower
    
    if a == 'swim':
        print("game over")
    else:
        door = input("Which door ? red blue yellow ")
        if door == "red" or door == "blue":
            print("game over")
        else:
            print("you win")
else:
    print("game over")
    