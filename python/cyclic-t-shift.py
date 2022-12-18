def solution(nums):
	print(f'\nnums = {nums}')
	len_nums = len(nums)
	min_val = min(nums)
	max_val = max(nums)

	min_val_index = len_nums - 1 - nums[::-1].index(min_val)
	max_val_index = nums.index(max_val)

	print(f'len_nums = {len_nums}, min_val = {min_val}, max_val = {max_val}, min_val_index = {min_val_index}, max_val_index = {max_val_index}')
	if((min_val_index + 1) % len_nums) != max_val_index:
		print('min_val_index and max_val_index not adjacent')
		return(-1) 

	for i in range(len_nums-1):
		print(f'(i+max_val_index)%len_nums = {(i+max_val_index)%len_nums}, (i+1+max_val_index)%len_nums = {(i+1+max_val_index)%len_nums}')
		if nums[(i+max_val_index)%len_nums] < nums[(i+1+max_val_index)%len_nums]:
			print('values not in descending order')
			return(-1)

	return(max_val_index)


if __name__ == "__main__":
	print(f"solution([5,4,3,2,1]) = {solution([5,4,3,2,1])}\n")
	print(f"solution([1,5,4,3,2]) = {solution([1,5,4,3,2])}\n")
	print(f"solution([3,2,1,5,4]) = {solution([3,2,1,5,4])}\n")
	print(f"solution([4,3,2,1,5]) = {solution([4,3,2,1,5])}\n")
	print(f"solution([3,2,1,0,6,5,4]) = {solution([3,2,1,0,6,5,4])}\n")

	print(f"solution([3,2,1,6,6,5,4]) = {solution([3,2,1,6,6,5,4])}\n")
	print(f"solution([3,1,1,6,6,5,4]) = {solution([3,1,1,6,6,5,4])}\n")
	print(f"solution([4,2,1,0,6,5,4]) = {solution([4,2,1,0,6,5,4])}\n")

	print(f"solution([5,6,4,3,2,1]) = {solution([5,6,4,3,2,1])}\n")
	print(f"solution([6,1,5,4,3,2]) = {solution([6,1,5,4,3,2])}\n")
	print(f"solution([3,6,2,1,5,4]) = {solution([3,6,2,1,5,4])}\n")
	print(f"solution([4,3,2,1,5,6]) = {solution([4,3,2,1,5,6])}\n")
	print(f"solution([3,2,1,0,6,5,6,4]) = {solution([3,2,1,0,6,5,6,4])}\n")
