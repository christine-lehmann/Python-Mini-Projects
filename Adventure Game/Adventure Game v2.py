def scene1():
    import time
    print("\n\tWELCOME TO THIS ADVENTURE GAME!\n"
          "\n\tLet's start the action! ☆-🎬-☆\n"
          "\n\t\tLily wakes up in her bedroom in the middle of the night. She heard a loud BAN outside the house."
          "\n\t\tNow she has two choices she can either stay in the room or check what the sound might be about.")
    c1 = input("\n\n\tType your choice: Stay or Evaluate? ")

    time.sleep(2)
    ans = 'incorrect'
    while (ans == 'incorrect'):
        if (c1.upper() == "STAY"):
            print(
                "\n\tLily decides to stay in the room and ends up staying inside forever as noone seems to come to help her.")
            ans = 'correct'
        elif (c1.upper() == "EVALUATE"):
            print("\n\tLily exits the room silently and reaches the main hall.")
            ans = 'correct'
            scene2()
        else:
            c1 = input("\tENTER THE CORRECT CHOICE! Stay or Evaluate?: ")


def scene2():
    import time
    print("\n\t\tIn the main hall, she finds a strange but cute teddy bear on the floor. "
          "\n\t\tShe wanted to pick the teddy up. "
          "\n\t\tBut should she? It doesn't belong to her. (•˳̂•̆)")
    time.sleep(2)
    c1 = input("\n\n\tType your choice: Pick or Ignore?: ")


    ans = 'incorrect'
    while (ans == 'incorrect'):
        if (c1.upper() == "PICK"):
            print(
                "\n\t\tThe moment Lily picked up the the teddy bear. The Teddy bear starts TALKING!"
                "\n\t\tThe bear tells Lily that she is in grave danger as there is a monster in the house."
                "\n\t\tAnd the monster has captured her PARENTS as well!"
                "\n\t\tBut he hugged her and told her not to get scared as he knows how to beat the moster!")
            time.sleep(2)
            print("\n\tThe bear handed lily a magical potion which can weaken the moster and make him run away!"
                  "\n\t\tHe handed her the potion and then DISAPPEARED! Lily moved forward.")
            ans = 'correct'
            pick = "True"
        elif (c1.upper() == 'IGNORE'):
            print("""\n\tLily decided not to pick up the bear and walked forward.""")
            ans = 'correct'
            pick = "False"
        else:
            c1 = input("\tWrong Input! Enter pick or ignore?: ")
    time.sleep(2)
    scene3(pick)


def scene3(pick_value):
    import time
    print("\n\n\tAfter walking for a while, Lily saw the MONSTER in front of her!"
    "\n\t\tIt had red eyes and evil looks. She got very scared! ")
    time.sleep(2)
    if (pick_value == "True"):
        time.sleep(2)
        print("\n\tBut then she remembered! She had the magic portion and she threw it on the moster!"
              "\n\t\tWell she had nothing to lose!""")
        time.sleep(2)
        print("\n The monster SCREAMED in pain but he managed to make a portal and pushed Lily to a new world!")
    elif (pick_value == "False"):
        print("\n\tThe monster attacked Lily and hurt her! She was then thrown to the new world by the monster!")


if __name__ == "__main__":
    scene1()
print("\n\n")
print("=================================END OF CHAPTER 1=================================")

# Original Source: https://www.askpython.com/python/text-based-adventure-game

