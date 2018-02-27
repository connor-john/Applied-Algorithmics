"""
Connor Taylor
Compsci 320 Assignment1
"""

def pair(numbers):
	numbers.sort()
	sum = numbers[-1] * 2
	sums = {}
	count = len(numbers)
	for i in range(0, count - 1):
		a = numbers[i]
		if a >= sum:
			break
		for j in range(i + 1, count):
			b = numbers[j]
			if b >= sum:
				break
			temp = a + b
			if temp in sums:
				if temp < sum:
					sum = temp
					break
			elif temp >= sum:
				break
			else:
				sums[temp] = 1
	if sum == numbers[-1] * 2:
		return None
	else:
		return sum

def main():
	while True:
		line = input()
		if line == "0":
			break
		numbers = line.split()
		numbers = [int(number) for number in numbers]
		total = pair(numbers)
		if total is None:
			print(None)
		else:
			print("yes: " + str(total))

main()
