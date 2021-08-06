import sys

# collatz sequence takes any integer and works its way to one, using only two operations:
# if the integer if even it is divided by two
# if the integer is odd it's multiplied by 3 and 1 is added
# This program can either run recursively, starting with a large number and testing every
# lower number. Or run once based on a user entered number.


# Global Variables:
    # For the automated version this is the number which collatz() will start at.
testNumber = int(input("Enter a starting integer: "))
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
else:
    while testNumber != 1:
        testingInt = testNumber
        while testingInt != 1:
            testingInt = collatz(testingInt)
        else:
            print(str(testNumber) + " Works")
            testNumber += - 1