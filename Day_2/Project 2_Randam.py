#project  Rock Paper Scssors
import random
rock = ''''
----.________
      ______)
      (______)
      (_______)
      (______)
----.__(____)
      '''

paper = '''
___'-----
      ___)____
        _______)
        ________)
      _________)
---._________)
'''


scssors ='''
______|----
        ___)____
          ______)
        __________)
        _____)
-----.____)
'''

game_img = [rock,paper,scssors]
user_choice = int(input("What do yoy choose ? type 0 rock,1 for papre, 2 scissor..   "))
print(game_img[user_choice])

computer_choice = random.randint(0,2)
print("computer_chose :") 
print(game_img[computer_choice])

if user_choice >= 3 or user_choice <0: 
    print("You type invalide Number.You lose.")
elif user_choice == 0 and computer_choice == 2:
    print("You win...!")
elif computer_choice == 0 and user_choice==2:
    print("You Lose..!")
elif computer_choice > user_choice:
    print("you Lose..!")
elif user_choice > computer_choice:
    print("You Win..!")
elif computer_choice == user_choice:
    print("It's draw")
