def get_combo (x):
	x_str = str(x)
	x_len = len(x_str)
	combo = [x]
	for i in range(x_len):
		for j in range(i+1, x_len):
			combo += [int(x_str[0:i] + x_str[j] + x_str[i+1:j] + x_str[i] + x_str[j+1:])]
	return(list(set(combo) - set([x])))


def check_order (numbers, num_count, curr_index, swap_available):
	print(f'numbers = {numbers}, num_count = {num_count}, curr_index = {curr_index}, swap_available = {swap_available}')
	if curr_index == (num_count - 1):
		return(True)

	if (swap_available == False):
		if (numbers[curr_index] >= numbers[curr_index + 1]):
			return(False)
		return(check_order(numbers[:], num_count, curr_index + 1, False))

	res = False
	combo = [numbers[curr_index + 1]] + get_combo(numbers[curr_index + 1])
	print(f'combo[{curr_index + 1}] = {combo}')
	for num in combo:
		new_list = numbers[0:curr_index + 1] + [num] + numbers[curr_index + 2:]
		res = check_order(new_list[:], num_count, curr_index, False) or res
	return(res)


def solution (numbers):
	print(f'\n\nCalling solution({numbers})')

	num_count = len(numbers)
	if num_count == 0:
		return(False)

	if num_count == 1:
		return(True)	

	res = check_order(numbers[:], num_count, 1, True)
	combo = get_combo(numbers[0])
	print(f'\ntop combo[{numbers[0]}] = {combo}')
	for num in combo:
		res = check_order([num]+numbers[1:], num_count, 1, False) or res
	return(res)


if __name__ == '__main__':
	"""
	print(f'combo(0) = {get_combo(0)}')
	print(f'combo(1) = {get_combo(1)}')
	print(f'combo(23) = {get_combo(23)}')
	print(f'combo(66) = {get_combo(66)}')
	print(f'combo(123) = {get_combo(123)}')
	print(f'combo(1) = {get_combo(1)}')
	print(f'combo(3456) = {get_combo(3456)}')
	print(f'combo(1111) = {get_combo(1111)}')
	print(f'combo(77889) = {get_combo(77889)}')
	print(f'combo(4030400) = {get_combo(4030400)}')

	"""

	print('')
	numbers = []
	print(f"solution({numbers}) = {solution(numbers)}\t Expected = False\n")

	print('')
	numbers = [20]
	print(f"solution({numbers}) = {solution(numbers)}\t Expected = True\n")

	print('')
	numbers = [1,5,10,20]
	print(f"solution({numbers}) = {solution(numbers)}\t Expected = True\n")

	print('')
	numbers = [100,3,900,10]
	print(f"solution({numbers}) = {solution(numbers)}\t Expected = True\n")

	print('')
	numbers = [1,3,900,9]
	print(f"solution({numbers}) = {solution(numbers)}\t Expected = False\n")

	print('')
	numbers = [1,3,900,709]
	print(f"solution({numbers}) = {solution(numbers)}\t Expected = True\n")

	print('')
	numbers = [100,3,9,10]
	print(f"solution({numbers}) = {solution(numbers)}\t Expected = True\n")

	print('')
	numbers = [13,31,30]
	print(f"solution({numbers}) = {solution(numbers)}\t Expected = False\n")

	#"""
