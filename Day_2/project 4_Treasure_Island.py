print("Welcome to Treasure Island ")
print("You mission  is to find the Treasure Island...")
choice1=input('you\'re at crossroad , Whare do you want to go ?'
              'Type "left" or "right" . \n').lower()
if choice1 == "left":
    choice2 = input('you\'ve come to lake..'
                    'there is a island in the middel of  the lake .'
                    'Type "wait" fore a boat..'
                    'type "swim" to swim  across ... \n ').lower()
    if choice2 == "wait":
        choice3 = input("You arrive  at the  island unharmed ."
                      "There  is  house with three doors. ones red "
                        "one yellow and one blue. "
                          "Wich color do you choose ."  ).lower()
        if choice3=="red":
            print("It's a room fill of fire. Game over ..!")
        elif choice3 == "yellow":
            print("you found the Treasur. you win..!")
        elif choice3 =="blue":
            print("you enter a room of beasts.Game over..!")
        else:
            print("you chose a door that doesn't exist .Game over...!")
    else:
        print("You got attecked by angry trout. Game over....!")
else:
    print("you Fell in to a whole Game over...!")