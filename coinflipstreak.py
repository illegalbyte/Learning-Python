import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinflipList = []
    for coinflip in range(100):
    	coinflipList.append( random.choice(['H','T']) )

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in coinflipList:
        sixTestFlips = []
        for x in range(0,6):
            # add the current flip value (h/t) plus the folowing 6 values to sixTestFlips
            sixTestFlips.append(coinflipList[coinflipList.index(i) + x])
            print(sixTestFlips)
        if sixTestFlips == ['T','T','T','T','T','T'] or sixTestFlips == ['H','H','H','H','H','H']:
            numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))