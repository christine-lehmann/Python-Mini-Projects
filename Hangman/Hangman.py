import random

from words import word_list # imported from words.py file

def get_valid_word():
    word = random.choice(word_list) #randomly chooses something from the list
    return word.upper()

def play(word):
    word_complete = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    name = input("What is your name? ")
    print("Hello " + name + "! Let's Play Hangman!")
    print(display_hangman(tries))
    print(word_complete)
    print('\n')

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Oops! You've already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -=1
                guessed_letters.append(guess)
            else:
                print("Good job!", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_complete)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_complete = "".join(word_as_list)
                if "_" not in word_complete:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Oops! You've already guessed the word", guess)
            elif guess != word:
                print(guess, "is not in the word.")
                tries =1
                guessed_words.append(guess)
            else:
                guessed = True
                word_complete = word
        else:
            print('Not a valid guess.')
        print(display_hangman(tries))
        print(word_complete)
        print('\n')
    if guessed:
        print("Woah, You won! :)")
    else:
        print("Sorry, you run out of tries. The word was " + word + ". Better luck next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_valid_word()
    play(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        word = get_valid_word()
        play(word)

print(main)
if __name__ == "__main__":
    main()
