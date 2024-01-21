def solution(a,b):
    answer = 0
    a.sort()
    b.sort()
    b.reverse()
    for i in range(len(a)):
        answer =  answer +  a[i] * b[i]
    
    return answer