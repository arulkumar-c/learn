def solution(numbers, left, right):
	result = []
	for i in range(len(numbers)):
		factor = int(numbers[i] / (i+1))
		if factor and ((numbers[i] % factor) == 0) and (left <= factor <= right):
			result += [True]
		else:
			result += [False]
	return(result)

if __name__ == "__main__":
	print(f'solution([8,5,6,16,5], 1, 3) = {solution([8,5,6,16,5], 1, 3)}')
	print(f'solution([4,4,4,4,4,4], 1, 3) = {solution([4,4,4,4,4,4], 1, 3)}')
