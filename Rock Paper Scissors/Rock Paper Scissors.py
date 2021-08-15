import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper','scissors']
print("\n")
print("\t=========================================")
print("\t=                                       =")
print("\t=      WELCOME TO ROCK, PAPER,          =")
print("\t=         AND SCISSORS GAME             =")
print("\t=                                       =")
print("\t=========================================")


while True:
    user_input = input('\nRock '
                       '\nPaper '
                       '\nScissors '
                       '\nQ to quit'
                       '\nYour Pick: ').lower()
    if user_input == 'q':
        break

    if user_input not in ['rock', 'paper','scissors']:
        print("Choose only from the options.\n")
        continue
    random_num = random.randint(0,2)
    #rock: 0, paper: 1, scissors: 2
    ai_pick = options[random_num]
    print('AI picked', ai_pick + ".")

    if user_input == 'rock' and ai_pick == 'scissors':
        print("You won!")
        user_wins += 1

    elif user_input == 'paper' and ai_pick == 'rock':
        print("You won!")
        user_wins += 1

    elif user_input == 'scissors' and ai_pick == 'paper':
        print("You won!")
        user_wins += 1

    elif user_input == ai_pick:
        print("Draw")

    else:
        print("You lose!")
        computer_wins += 1

print("\nYou won", user_wins, "times.")
print("The AI won", computer_wins, "times.")
print("Ciao!")


if __name__ == "__main__":
    print()