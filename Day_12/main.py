# Number Guessing Game 

from random import randint
EASY_LEVEL = 10
HARD_LEVEL = 5



#Function to check the users guess against the actual answer
def check_answer(user_guess , actual_answer, turns):
    """Checks the answer against the guess. Returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it!  The answer was {actual_answer} .")


#Function to set Difficulty 
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return  EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    # Choose a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")   
    print("I'm thinking of  a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")


    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining  to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
    # Track the number of turns and reduce by 1 if they get it wrong

game()