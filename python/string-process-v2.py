def solution (sa, sb):
	print(f'sa = \'{sa}\', sb = \'{sb}\'')

	char_count_sa = {}
	char_count_sb = {}

	for c in set(sa):
		char_count_sa |= {c:sa.count(c)}

	for c in set(sb):
		char_count_sb |= {c:sb.count(c)}

	print(f'char_count_sa = {char_count_sa}')
	print(f'char_count_sb = {char_count_sb}')

	res =''
	lena = len(sa)
	lenb = len(sb)
	ia = ib = 0
	while (ia < lena) and (ib < lenb):
		if char_count_sa[sa[ia]] == char_count_sb[sb[ib]]:
			if (sa[ia] == sb[ib]) or (sa[ia] < sb[ib]):
				res += sa[ia]
				ia += 1
			else:
				res += sb[ib]
				ib += 1
		elif char_count_sa[sa[ia]] < char_count_sb[sb[ib]]:
			res += sa[ia]
			ia += 1
		else:
			res += sb[ib]
			ib += 1

		if (ia == lena) and (ib != lenb):
			res += sb[ib:]
			ib = lenb
		elif (ib == lenb) and (ia != lena):
			res += sa[ia:]
			ia = lena

	return(res)


if __name__ == '__main__':
	print('')

	sa = 'dce'
	sb = 'cccbd'
	print(f"solution({sa}, {sb}) = {solution(sa, sb)}\n")

	sa = 'super'
	sb = 'tower'
	print(f"solution({sa}, {sb}) = {solution(sa, sb)}\n")

	sa = 'applebeesoup'
	sb = 'bananamilkshake'
	print(f"solution({sa}, {sb}) = {solution(sa, sb)}\n")
