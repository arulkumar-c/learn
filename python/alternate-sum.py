"""
Given an integer n. our task is to calculate the alternating sum of its digits. In other words, add up all the digits, taking the
first digit with a positive sign, the second digit with a negative sign, the third digit with a positive sign, etc.

n = 9236

t = 9 - 2 + 3 - 6 = 4
"""

def solution(n):
	total = 0
	num_digits = 0
	last_sign_is_plus = False
	while n:
		d = n % 10
		n = int(n/10)
		num_digits += 1
		if num_digits % 2:
			total += d
			last_sign_is_plus = True
		else:
			total -= d
			last_sign_is_plus = False

	if last_sign_is_plus == False:
			total = -total
	return(total)


if __name__ == "__main__":
	print(f'solution(12345) = {solution(12345)}')
	print(f'solution(612345) = {solution(612345)}')
	print(f'solution(9236) = {solution(9236)}')

