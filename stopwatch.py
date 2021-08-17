#! python3
# stopwatch.py - Simple stopwatch, counts seconds between hitting enter

import time

# display instructions
print('Press ENTER to begin. Then press ENTER to \'click\' the stopwatch. Ctr-C to quit.')

input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times
try: 
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print(f'Lap {lapNum}: {totalTime} ({lapTime})')
		lapNum += 1
		lastTime = time.time()
except KeyboardInterrupt:
	print('\nDone 😎')