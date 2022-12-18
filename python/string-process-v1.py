
def solution (sa, sb):
	res =''
	lena = len(sa)
	lenb = len(sb)
	ia = ib = 0
	while (ia < lena) and (ib < lenb):
		if sa[ia] == sb[ib]:
			res += sa[ia]
			ia += 1
			res += sb[ib]
			ib += 1
		elif sa[ia] < sb[ib]:
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
	sa = 'super'
	sb = 'tower'
	print(f"solution({sa}, {sb}) = {solution(sa, sb)}\n")

	sa = 'applebeesoup'
	sb = 'bananamilkshake'
	print(f"solution({sa}, {sb}) = {solution(sa, sb)}\n")
