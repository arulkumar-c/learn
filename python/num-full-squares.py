def dummy(a,b):
	res = a+b*100

from math import sqrt

def solution (nums):
	print(f'nums = {nums}\t\tlen(nums) = {len(nums)}')
	res = 0
	
	nums_len = len(nums)

	for i in range(nums_len):
		print(f'len(nums[{i}:]) = {len(nums[i:])}')
		for j in range(i, nums_len):
			print(f'\n{i}, {j}: {nums[i]}, {nums[j]}', end='\t')
			sums = nums[i] + nums[j]
			print(f'sums = {sums}', end='\t')
			if sums >= 0:
				sq_root = sqrt(sums)
				print(f'sq_root = {sq_root}', end='\t')
				if sq_root == int(sq_root):
					res += 1
					print(f'res = {res}', end='\t')

	print('')
	return(res)


if __name__ == '__main__':
	print('')
	nums = [-1,18,3,1,5]
	print(f"solution() = {solution(nums)}\n")

	print('')
	nums = [2]
	print(f"solution() = {solution(nums)}\n")

	print('')
	nums = [-2,-1,0,1,2]
	print(f"solution() = {solution(nums)}\n")

