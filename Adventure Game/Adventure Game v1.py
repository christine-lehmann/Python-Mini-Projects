import time

name = input("What is your name? ")
age = int(input("What is your age? "))

if age >= 12:
    print("Starting...\n")
    time.sleep(1)  # Adding delays for extra effects
    print("Please wait!")
    time.sleep(1)
    count = 0
    while count != 5:
        print(".", end="")
        time.sleep(2 / 5)
        count += 1

    print("\nHello", name, "! Welcome to this adventure! 🏕️🏝️🏖️🏕")

    answer = input("\nYou are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go (left/right)?: ").lower()

    if answer == "left":
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2 / 5)
            count += 1
        answer = input("\nYou come to a river, you can walk around it or swim accross? Type W to walk around and S to swim accross: ").upper()

        if answer == "S":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            print("\nYou swam acrross and were eaten by an alligator.")
        elif answer == "W":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            print("\nYou walked for many miles, ran out of water and you lost the game.")
        else:
            print('Not a valid option. You lose.')

    elif answer == "right":
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2 / 5)
            count += 1
        answer = input("\nYou come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

        if answer == "back":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            print("\nYou go back and lose.")
        elif answer == "cross":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            answer = input("\nYou cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()

            if answer == "yes":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2 / 5)
                    count += 1
                print("\nYou talk to the stanger and they give you gold. You WIN!")
            elif answer == "no":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2 / 5)
                    count += 1
                print("\nYou ignore the stranger and they are offended, You LOSE!.")
            else:
                print('Not a valid option. You lose.')
        else:
            print('Not a valid option. You lose.')

    else:
        print('Not a valid option. You lose.')

    print("Thank you for trying", name, ":)")
else:
    print("\nI'm sorry :( You are not old enough to play...")
    print("\nExiting...")
    count = 0
    while count != 5:
        print(".", end="")
        time.sleep(2/5)
        count += 1
    print()

if __name__ == "__main__":
    print()