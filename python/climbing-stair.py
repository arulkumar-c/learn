"""
You are climbing a staircase that has n
steps. You can take the steps either 1 or 2
at a time. Calculate how many distinct ways
you can climb to the top of the staircase.
"""

def num_ways (curr_step, target_steps):
	if curr_step == target_steps:
		return(1)

	if curr_step > target_steps:
		return(0)

	return(num_ways(curr_step+1, target_steps) + num_ways(curr_step+2, target_steps))

def solution (target_steps):
	return(num_ways(0, target_steps))


if __name__ == "__main__":
	print('')
	print(f"solution(1) = {solution(1)}\n")
	print(f"solution(2) = {solution(2)}\n")
	print(f"solution(3) = {solution(3)}\n")
	print(f"solution(4) = {solution(4)}\n")
	print(f"solution(5) = {solution(5)}\n")
	print(f"solution(10) = {solution(10)}\n")

