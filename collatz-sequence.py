import sys

def collatz(number):
    if (int(number) % 2 == 0):
        print(str(int(number) // 2))
        return int(number) // 2
    else:
        print(str(3 * int(number) + 1))
        return 3 * int(number) + 1


version = input("(r) or (input)?")
testNumber = 500000000000000000000000000000000000000000000000000000000000000000

if version == 'input':
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
            testNumber = testNumber - 1