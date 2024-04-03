def solution(list):
    answer = 0
    result = []
    list.sort()
    num = 1
    
    while True:
        a = list[-1] * num
        count = 0
        for i in list:
            if a % i == 0: # 끝원소와 배열의 원소중 배수라면
                count += 1
            else:
                break
        if count == len(list):
            return a
        num += 1
