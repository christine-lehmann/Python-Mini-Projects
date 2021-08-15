def madlib():
    per_name = input("\n\nPerson's Name: ")
    place = input("Place: ")
    verb1 = input("Verb: ")
    animal = input("Animal: ")
    exer = input("An Exercise: ")
    noun1 = input("Noun: ")
    face = input("Part of Face: ")
    adj1 = input("Adjective: ")
    vege = input("Vegetable: ")
    act = input("Activity: ")
    verb2 = input("Verb: ")
    verb3 = input("Verb: ")
    noun2 = input("Noun: ")
    famous = input("Famous Person: ")

    madlib = f"\nDear, {per_name}. \nI am writing this email to informed you that something funny happened at \
{place}. \nWhen I was, {verb1} the trash out, I stumbled upon a {animal} doing push-ups and {exer}.\
\nThis {noun1} was dressed in a bunny costume. \nIt had a large {face} and a cute {adj1} tail. \
\nI asked this {vege} head what was he doing by the trash cans? \nHe replied, \"I'm training for the  \
Easter Day {act}. \nRabbits always win, so I thought I would {verb2} like one and maybe finally win!\" \
\nI said, \"Well Goodluck! I hope you {verb3} like the {noun2}.\" \
\nYour Friend, {famous}. :)"

    print(madlib)

if __name__ == '__main__':
    madlib()