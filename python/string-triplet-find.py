def solution(s):
	count = 0
	for i in range(len(s)-2):
		if(len(set(s[i:i+3]))) == 3:
			count += 1
	return(count)

if __name__ == "__main__":
	print(f"solution('abcdaaae') = {solution('abcdaaae')}")
	print(f"solution('aabbccddee') = {solution('aabbccddee')}")
