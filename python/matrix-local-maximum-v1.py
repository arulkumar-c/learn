def sub_mat_compute (matrix, co_ords):
	# co_ords = (row, col)
	#
	# sub_mat = {'row_start', 'row_len', 'col_start', 'col_len', 'exclude_list' = [(x,y). (a,b),...]}

	r = co_ords[0]
	c = co_ords[1]
	val = matrix[r][c]

	if val == 0:
		return(None)

	row_total = len(matrix)
	col_total = len(matrix[0])

	row_start = (r - val) if (r - val) >= 0 else 0
	row_end =   (r + val) if (r + val) < row_total else row_total-1
	row_len = (row_end+1) - row_start

	col_start = (c - val) if (c - val) >= 0 else 0
	col_end =   (c + val) if (c + val) < col_total else col_total-1
	col_len = (col_end+1) - col_start

	exclude_list = [(r, c)]
	if(row_start == (r - val)) and (col_start == (c - val)):
		exclude_list += [(r - val, c - val)]
	if(row_start == (r - val)) and (col_end == (c + val)):
		exclude_list += [(r - val, c + val)]
	if(row_end == (r + val)) and (col_start == (c - val)):
		exclude_list += [(r + val, c - val)]
	if(row_end == (r + val)) and (col_end == (c + val)):
		exclude_list += [(r + val, c + val)]

	sub_mat = {'row_start':row_start, 'row_len':row_len, 'col_start':col_start, 'col_len':col_len, 'exclude_list':exclude_list}
	#print(f'co_ords = {co_ords}, sub_mat = {sub_mat}')
	return(sub_mat)
	

def max_val (matrix, sub_mat):
	row_start = sub_mat['row_start']
	col_start = sub_mat['col_start']
	row_len = sub_mat['row_len']
	col_len = sub_mat['col_len']
	exclude_list = sub_mat['exclude_list']
	
	mv = None
	for r in range(row_start, row_start + row_len):
		for c in range(col_start, col_start + col_len):
			if (r, c) in exclude_list:
				#print(f'max : exclude_list : ({r}, {c}')
				continue
			if (not mv) or (mv < matrix[r][c]):
				mv = matrix[r][c]
	#print(f'max_val: sub_mat = {sub_mat}, mv = {mv}')
	return(mv)

"""
def get_next_coord (matrix, sub_mat, curr_coord):
	row_start = sub_mat['row_start']
	col_start = sub_mat['col_start']
	row_len = sub_mat['row_len']
	col_len = sub_mat['col_len']
	exclude_list = sub_mat['exclude_list']
	
	curr_r = curr_coord[0]
	curr_c = curr_coord[1]

	for r in range(row_start, curr_r + 1):
		if ((r, curr_c) not in exclude_list:
			exclude_list += [(r, curr_c)]

	for r in range(curr_r, row_len - (curr_r - 1)):
		for c in range(col_start, col_start + col_len):
			if ((r, c) in exclude_list) or (matrix[r][c] == 0):
				continue
			return((r, c))
	return(None)
"""

def solution (matrix):
	if not matrix:
		return([])

	row_total = len(matrix)
	col_total = len(matrix[0])

	res = []
	for r in range(row_total):
		for c in range(col_total):
			sub_mat = sub_mat_compute(matrix, (r, c))
			if sub_mat and (matrix[r][c] > (mv := max_val(matrix, sub_mat))):
				res += [[r, c]]
			if sub_mat:
				print(f'({r}, {c}) ==> sub_mat = {sub_mat}, mv = {mv}, res = {res}')
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

