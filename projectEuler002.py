#! python3
# ProjectEUler.net Problem 2

def fibonacci():
	sequence = [1,2]
	while (sequence[-1] + sequence[-2]) < 4000000:
		sequence.append(sequence[-1] + sequence[-2])
		print(sequence[-1])
	return sequence

fibfourmillion = fibonacci()


evenFibNumbers = []
for i in fibfourmillion:
	if i % 2 == 0:
		print(i)
		evenFibNumbers.append(i)

print(sum(evenFibNumbers))
