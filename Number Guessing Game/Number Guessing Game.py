import random

print("\t==========================================")
print("\t=                                        =")
print("\t=    WELCOME TO NUMBER GUESSING GAME     =")
print("\t=                                        =")
print("\t==========================================")
top_of_range = input("\nType a number for an upper bound: ")

if top_of_range.isdigit():
    print("\n☆☆☆☆☆☆☆☆☆☆☆ L E T 'S P L A Y ! ☆☆☆☆☆☆☆☆☆☆☆")
    top_of_range = int(top_of_range)
else:
    print("Please type a number next time.\n")
    quit()

random_num = random.randint(0, top_of_range)

guess = None
count = 1

while True:
    guess = input("\nPlease type a number between 1 and " + str(top_of_range) + ': ')
    if guess.isdigit():
        guess = int(guess)

        if guess == random_num:
            print("\nYou got it!")
            break
        if guess != random_num:
            #print('You got it wrong!')
            if guess < random_num:
                print("Your guess is too low. Try again.")
                count += 1
            elif guess > random_num:
                print("Your guess is too high. Try again.")
                count += 1
    else:
        print("Please type a number next time.")


print('It took you', count, "guess/guesses!")


if __name__ == "__main__":
    print()
