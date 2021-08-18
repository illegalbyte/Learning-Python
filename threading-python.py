import threading, time

print('1. Start')

def takeANap(length):
	time.sleep(length)
	print('2. Wake up')

threadObj = threading.Thread(target=takeANap, args=[int(input('Enter time: '))])

threadObj.start()

print('3. End of program')