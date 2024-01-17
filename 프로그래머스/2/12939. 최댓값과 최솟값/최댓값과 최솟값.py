def solution(s):
    answer = ''
    answer = list(map(int, s.split()))
    min_answer = min(answer)
    max_answer = max(answer)
    answer = str(min_answer)+ " " + str(max_answer)

    return answer


