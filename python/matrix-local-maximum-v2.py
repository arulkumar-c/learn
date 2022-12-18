def sub_mat_compute_max (matrix, curr_row, curr_col):
	val = matrix[curr_row][curr_col]
	if val == 0:
		return(0)

	row_total = len(matrix)
	col_total = len(matrix[0])

	row_start = (curr_row - val) if (curr_row - val) >= 0 else 0
	row_end =   (curr_row + val) if (curr_row + val) < row_total else row_total-1
	row_len = (row_end+1) - row_start

	col_start = (curr_col - val) if (curr_col - val) >= 0 else 0
	col_end =   (curr_col + val) if (curr_col + val) < col_total else col_total-1
	col_len = (col_end+1) - col_start

	exclude_list = [(curr_row, curr_col)]
	if(row_start == (curr_row - val)) and (col_start == (curr_col - val)):
		exclude_list += [(curr_row - val, curr_col - val)]
	if(row_start == (curr_row - val)) and (col_end == (curr_col + val)):
		exclude_list += [(curr_row - val, curr_col + val)]
	if(row_end == (curr_row + val)) and (col_start == (curr_col - val)):
		exclude_list += [(curr_row + val, curr_col - val)]
	if(row_end == (curr_row + val)) and (col_end == (curr_col + val)):
		exclude_list += [(curr_row + val, curr_col + val)]
	
	max_val = None
	for r in range(row_start, row_start + row_len):
		for c in range(col_start, col_start + col_len):
			if (r, c) in exclude_list:
				continue
			if (max_val == None) or (max_val < matrix[r][c]):
				max_val = matrix[r][c]
	return(max_val)


def solution (matrix):
	if not matrix:
		return([])

	row_total = len(matrix)
	col_total = len(matrix[0])

	res = []
	for r in range(row_total):
		for c in range(col_total):
			if matrix[r][c] > sub_mat_compute_max(matrix, r, c):
				res += [[r, c]]
	return(res)


if __name__ == "__main__":
	print('')
	matrix = [
		[3,0,1,0,0,0,0,0,3],
		[0,2,0,0,0,0,0,0,1],
		[0,0,1,0,0,0,2,0,0],
		[1,0,2,3,0,0,0,0,0],
		[0,0,3,0,0,0,0,0,2],
		[0,0,0,0,0,2,0,0,0],
		[0,0,1,0,0,0,0,0,0],
		[0,0,0,0,4,0,0,0,0],
		[3,0,0,0,0,0,0,0,3]
	]

	print("""
        0 1 2 3 4 5 6 7 8
    
    0  [3,0,1,0,0,0,0,0,3],
    1  [0,2,0,0,0,0,0,0,1],
    2  [0,0,1,0,0,0,2,0,0],
    3  [1,0,2,3,0,0,0,0,0],
    4  [0,0,3,0,0,0,0,0,2],
    5  [0,0,0,0,0,2,0,0,0],
    6  [0,0,1,0,0,0,0,0,0],
    7  [0,0,0,0,4,0,0,0,0],
    8  [3,0,0,0,0,0,0,0,3]
""")
	print(f"solution(matrix) = {solution(matrix)}\n")

