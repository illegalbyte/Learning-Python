#! python3
# projectEuler0001.py 

from typing import no_type_check


multiplesOf3or5 = []

for number in range(1000):
	if number == 0: continue

	if number % 3 == 0 or number % 5 == 0: 
		multiplesOf3or5.append(number)


print(sum(multiplesOf3or5))