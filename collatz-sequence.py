import sys

def collatz(number):
    if (int(number) % 2 == 0):
        print(str(int(number) // 2))
        return int(number) // 2
    else:
        print(str(3 * int(number) + 1))
        return 3 * int(number) + 1

while True:
    try:
        userInput = int(input("Enter a number: "))

        while userInput != 1:
            userInput = collatz(userInput)
    except ValueError:
        print('Invalid input, enter an integer.')
    except KeyboardInterrupt:
        raise sys.exit()