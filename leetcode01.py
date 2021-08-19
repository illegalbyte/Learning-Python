#! python3 

# leetcode01.py - solution for problem one leetcode.com in python.


def twoSum(nums, target):
	for i1, number1 in enumerate(nums):
		for i2, number2 in enumerate(nums):
			if number1 + number2 == target and i1 is not i2:
				returnList = []
				returnList.append(i1)
				returnList.append(i2)
				return returnList


twoSum(nums=[3, 3], target=6)
