def add2 (a, b):
	return (a+b+1)

def add1 (a, b):
	res = add2(a,b)
	return (res)

def valid_paren (paren_list):

	print(paren_list)

	if ((len(paren_list) % 2) != 0):
		return False


	open_paren_all = ['{', '[', '(']
	close_paren_pair = {'}':'{', ']':'[', ')':'('}

	open_paren_list = []

	for paren in paren_list:
		res = add1(4, 6)
		#breakpoint();
		#print(break_varaiable)
		print(open_paren_list)
		if paren in open_paren_all:
			open_paren_list.append(paren)
		elif close_paren_pair[paren] != open_paren_list.pop():
			return False
	return True



paren_str = input("Enter the parentheses list: ")
paren_list = list(paren_str)

res = valid_paren(paren_list)

if res:
	print("The entered parentheses string is: Valid")
else:
	print("The entered parentheses string is: Invalid")
