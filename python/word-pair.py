def solution (words):
	print(f'words before sort() = {words}')
	words.sort()
	print(f'words after sort() = {words}')

	num_words = len(words)
	res = 0
	for i in range(num_words):
		j = i + 1
		while (j < num_words) and (words[i] == words[j][0:len(words[i])]):
			res += 1
			j += 1
	return(res)


if __name__ == '__main__':
	print('')
	words = ["back", "backdoor", "gammon", "backgammon", "comeback", "come", "door"]
	print(f"solution() = {solution(words)}\n")

	print('')
	words = ["abc", "a", "a", "b", "ab", "ac"]
	print(f"solution() = {solution(words)}\n")

	print('')
	words = ["duck", "duckback", "back", "backdoor", "gammon", "backgammon", "comeback", "come", "door"]
	print(f"solution() = {solution(words)}\n")

