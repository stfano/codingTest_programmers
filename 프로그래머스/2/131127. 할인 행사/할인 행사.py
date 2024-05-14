def solution(want, number, discount):

    want_num = {}
    for i in range(len(want)):
        want_num[want[i]] = number[i]
        
    result = 0

    for res in range(len(discount) - 9):
        count = 0
        for wan in want:
            if discount[res:res+10].count(wan) == want_num[wan]:
                count += 1
            if count == len(want):
                result += 1
    if result == 0 :
        return result
    else:
        return result