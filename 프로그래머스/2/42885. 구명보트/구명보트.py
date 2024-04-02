# def solution(p, l):
#     answer = 0
#     p.sort()
#     count = 0
#     for i in range(1, len(p)):
#     # print(i)
#         if p[0] + p[-i] <= l: # 50 + 80 < 100, 50 + 70 < 100, 50 + 50 < 100
#             p_ = p.pop(0)
#             p_ = p.pop(i-1)
#             # print(p)
#             count += 1

#     count += len(p)
#     return count

def solution(p, l):
    answer = 0
    p.sort()  
    left = 0  
    right = len(p) - 1 

    while left <= right:
        if p[left] + p[right] <= l:  
            left += 1  
        right -= 1  
        answer += 1  

    return answer