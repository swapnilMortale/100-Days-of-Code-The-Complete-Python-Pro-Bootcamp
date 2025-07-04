
# 7  project Hungman 

import random

stage = ['''
    +----+
    |    |
    0    |
   /|\   |
   / \   |
         |
        _|_
==========
''','''
    +----+
    |    |
    0    |
   /|\   |
   /     |
         |
        _|_
==========
''','''
    +----+
    |    |
    0    |
   /|\   |
         |
         |
        _|_
==========
''','''
    +----+
    |    |
    0    |
   /|    |
         |
         |
        _|_
==========
''','''
    +----+
    |    |
    0    |
    |    |
         |
         |
        _|_
==========
''','''
    +----+
    |    |
    0    |
         |
         |
         |
        _|_
==========
''','''
    +----+
    |    |
         |
         |
         |
         |
        _|_
==========
''']
logo = '''  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __   
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  
 | |  | | (_| | | | | (_| | | | | | | (_| | | | | 
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                     __/ |                      
                    |___/                       
'''
word_list = ["aardvark","baboon","camel"] # Create a List 

lives = 6

print(logo)
chosen_word = random.choice(word_list)    # chose a random word 
print(chosen_word)

placeholder = ""
word_len = len(chosen_word)

for position in range(word_len):    
    placeholder += "_"
print("Word To Guess : "+placeholder)

game_over = False

corect_letter = []

while not game_over:

    print(f"********************{lives} /6 Lives Left ***********************")
    guess = input("Guess a Letter  : ").lower()

    if guess in corect_letter:
        print(f"You've already  Guessed {guess}...")

    display  = ""

    for letter in chosen_word :
        if letter ==  guess:
            display  += letter
            corect_letter.append(guess)
        elif letter in corect_letter:
            display += letter
        else:
            display += "_"
    print("Word to Guess: ",display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} , that is not in the word.you loss a life.")

        if lives == 0:
            game_over = True
            print(f"**********IT WAS {chosen_word} ! YOU LOSE ***************")
    if "_" not in display:
        game_over = True
        print("**********************YOU WIN *************************")

    print(stage[lives])