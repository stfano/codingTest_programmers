def solution(n):
    answer = 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    list = [0] * (n + 1)
    list[1] = 1
    list[2] = 2
    
    for i in range(3, n + 1):
        list[i] = (list[i-1] + list[i-2])
        
    return list[n] % 1234567