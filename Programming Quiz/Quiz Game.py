from random import sample

print("\t=========================================")
print("\t=                                       =")
print("\t=   WELCOME TO PROGRAMMING QUIZ GAME    =")
print("\t=                                       =")
print("\t=========================================\n")


Questions = ['An extra piece of information that you pass to the function to customize it for a specific need. \nA. Selector\nB. Declaration\nC. Boundary\nD. Parameter ',
             'A connection that uses light to transmit information. \nA. Pixels\nB. Vectors\nC. Ethernet\nD. Fiber Optic ',
             'A number assigned to any item that is connected to the Internet. \nA. Algorithm\nB. IP Address\nC. Ping Address\nD. Binary ',
             'In coding this returns a value. \nA. Coding\nB. Programming\nC. Function\nD. Loop ',
             'A repetitive action or command typically created with programming loops. \nA. Repetition Command\nB. Iteration\nC. Loop\nD. None of the above ',
             'Cause the computer to execute the commands you\'ve written in your program. \nA. Debug\nB. Run\nC. Execute\nD. Process ',
             'An error in a program that prevents the program from running as expected. \nA. Rat\nB. Villain\nC. Bat\nD. Bug ',
             'Information. Often, quantities, characters, or symbols that are the inputs and outputs of computer programs. \nA. Bits\nB. Bugs\nC. Languages\nD. Data  ',
             'Pulling out specific differences to make one solution work for multiple problems. \nA. Conjunction\nB. Iteration\nC. Abstraction\nD. Conditional ',
             'Trying again and again, even when something is very hard. \nA. Persistemce\nB. Fighting\nC. Adversity\nD. Determination ',
             'The information about someone on the Internet. \nA. Resume\nB. Profile\nC. ID\nD. Digital Footprint ',
             'A piece of code that you can easily call over and over again. \nA. Iteration\nB. Loop\nC. Block\nD. Function ',
             'A way of representing information using only two options. \nA. Digits\nB. Binary\nC. Machine Language\nD. Code ',
             'The art of creating a program. \nA. Programming\nB. Coding\nC. Computer Science\nD. Computing ',
             'Statements that only run under certain conditions or situations. \nA. Invitations\nB. Request\nC. Conditionals\nD. Calls ',
             'A loop with a predetermined beginning, end, and increment (step interval). \nA. Do...While Loop\nB. Do...Until Loop\nC. For Loop\nD. For Next Loop ',
             'One or more commands or algorithm(s) designed to be carried out by a computer. \nA. Code\nB. Instructions\nC. Commands\nD. Steps ',
             'The action of doing something over and over again. \nA. Function\nB. Repetition Structure\nC. Loop\nD. Repeat Commands ',
             'Break a problem down into smaller pieces. \nA. Chunk\nB. Itemize\nC. Decompose\nD. Digest ',
             'A relatively easy-to-remember address for calling a web page (like www.code.org). \nA. HTTP\nB. DNS\nC. IP Address\nD. URL ',
             ]

Answers = ['D',
           'D',
           'B',  # <-- comma added
           'C',
           'B',
           'B',
           'D',
           'D',
           'C',
           'A',
           'D',
           'D',
           'B',
           'A',
           'C',
           'C',
           'A',
           'C',
           'C',
           'D'
           ]

right_ans = 0


# The zip function returns a generator, so we need to transform it to a list object for sample()
key = list(zip(Questions, Answers))

# Sample from key now instead of Questions
s = sample(key, 10)

for i in s:
    # in each "i" tuple [0] is the question, [1] is the answer
    print(i[0])
    user_answer = input('Answer: ')
    if user_answer.lower() == i[1].lower():
        print('Correct!!! +10 points\n')
        right_ans += 10
    else:
        print('Incorrect :(\n')
        right_ans -= 3

# Computing a final score
print('\nYou got {} points!! B O N U S +9'.format(right_ans))
# print("You got " + str((right_ans/ 10)* 100)+ "%.")


name = input("\nEnter your name: ")

file = open("scores.txt", "a")
file.write(str(right_ans+9) +"\t" + " | " + "\t" + name + "\n")
file.close()

file = open("scores.txt", "r")
lines = file.readlines()
# lines = file.split(",")
'''
if right_ans < 10:
       right_ans = str(right_ans)
       right_ans = right_ans.zfill(0)
else:
       pass'''

sortedData = (sorted(lines, reverse = True))

print("\n   L E A D E R B O A R D\n")
print("Position  Points |\tName")
for line in range(0, len(sortedData)):
    print("\t"+str(line+1)+"\t\t"+str(sortedData[line]),end=" ")

file.close()

if __name__ == '__main__':
    print()