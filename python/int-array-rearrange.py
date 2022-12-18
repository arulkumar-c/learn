def solution(a):
	len_a = len(a)
	print(f'a = {a}, len_a = {len_a}')

	b = []

	for i in range(len(a)):
		if (i%2) == 0:
			b += [a.pop(0)]
		else:
			b += [a.pop()]
	print(f'b = {b}')

	for i in range(len(b)-1):
		if b[i] >= b[i+1]:
			return(False)
	return(True)		

if __name__ == "__main__":
	print('')
	print(f"solution([]) = {solution([])}\n")
	print(f"solution([4]) = {solution([4])}\n")
	print(f"solution([4,5]) = {solution([4,5])}\n")
	print(f"solution([5,4]) = {solution([5,4])}\n")
	print(f"solution([5,4,3,2,1]) = {solution([5,4,3,2,1])}\n")
	print(f"solution([1,3,5,7,6,4,2]) = {solution([1,3,5,7,6,4,2])}\n")
	print(f"solution([1,3,5,7,8,6,4,2]) = {solution([1,3,5,7,8,6,4,2])}\n")
