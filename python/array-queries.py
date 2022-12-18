def solution (a, b, queries):
	print(f'a = {a}, b = {b}, queries = {queries}\n')

	res = []

	for query in queries:
		print(f'query = {query}', end='\t')
		if query[0] == 0:
			a[query[1]] = query[2]
			print(f'handled 0: a = {a}, b = {b}')
		elif query[0] == 1:
			complements = [query[1] - n for n in a]
			matches = [b.count(c) for c in complements]
			res += [sum(matches)]
			print(f'\thandled 1: res = {res}')

	print('')
	return(res)


if __name__ == '__main__':
	print('')
	a = [3,4]
	b = [1,2,3]
	queries = [[1,5], [0,0,1], [1,5]]
	print(f"solution() = {solution(a, b, queries)}\n")

	print('')
	a = [2,3]
	b = [1,2,2]
	queries = [[1,4], [0,0,3], [1,5]]
	print(f"solution() = {solution(a, b, queries)}\n")

