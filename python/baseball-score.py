def score_calc(score_list):
    print(score_list)

    actual_score = []

    for score in score_list:
        if score.isdigit():
            actual_score.append(int(score))
        elif score == '+':
            actual_score.append(actual_score[len(actual_score)-2] + actual_score[len(actual_score)-1])
        elif score == 'D':
            actual_score.append(2 * actual_score[len(actual_score)-1])
        elif score == 'C':
            actual_score.pop()
        print(actual_score)

    return(sum(actual_score))


score_str = input("Enter the score: ")

print("Total score is: ", score_calc(list(score_str)))

