import sys
# from colorama import Fore, Style, init #colorama required for easily displaying colored text
import random
import time
# init() # initialises colorama for windows

# collatz sequence takes any integer and works its way to one, using only two operations:
# if the integer if even it is divided by two
# if the integer is odd it's multiplied by 3 and 1 is added
# This program can either run recursively, starting with a number and testing every
# higher number. Or run once based on a user entered number.


# Global Variables:
    # For the automated version this is the number which collatz() will start at.


trials = 0

version = input("(r)ecursive or (i)nput? ")

# FUNCTIONS:
    # COLLATZ() takes any integer and works its way to 1.
def collatz(number):
    if (int(number) % 2 == 0):
        # print(str(int(number) // 2))
        return int(number) // 2
    else:
        # print(str(3 * int(number) + 1))
        return 3 * int(number) + 1

    # this function determines how the next number which will be tested will be determined
def getTestNumber():
    # testNumber = random.randint(2**40000, 2**50000)
    # return random.getrandbits(60000) ** 2
    # testNumber = int(input("Enter a large starting integer: "))
    return testNumber + 1



if version == 'i':
    while True:
        try:
            userInput = int(input("Enter a number: "))

            while userInput != 1:
                userInput = collatz(userInput)
        except ValueError:
            print('Invalid input, enter an integer.')
        except KeyboardInterrupt:
            raise sys.exit(0)
else: # if not (i), then (r)ecursive mode:
    while True: # Main loop
        testNumber = int(input("Enter a large starting integer: ")) # starting int
        while testNumber != 1: #if we haven't reached 1 do the following
            # print("Trying: " + Fore.RED + str(testNumber) + Style.RESET_ALL) #print the number we're trying
            print("(" + str(testNumber) +", ", end='')
            testingInt = testNumber #store our test number in a temporary value "testingInt"
            steps = 0 # keeps track of how many steps we take to reach 1
            while testingInt != 1: # loop which reaches 1 running collatz()
                testingInt = collatz(testingInt) # collatz the temporary testingInt
                steps += 1 #increase steps taken by one
            else: # if testingInt has reached one, do the following
                # print that it works
                #print(str(testNumber) + " Works, " + Fore.GREEN + str(steps) + Style.RESET_ALL + " step taken.")
                print(str(steps) + ")", end='\n')
                # set testNumber = to the next untested number using getTestNumber()
                testNumber = getTestNumber()
                #increase the count of trials we've run
                trials += 1
                time.sleep(0.001)