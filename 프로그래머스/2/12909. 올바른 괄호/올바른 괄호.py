def solution(s):
    count = 0
    for chars in s:
        if chars == "(":
            count += 1
            
        elif chars == ")":
            count -= 1
            
        if count < 0:
            return False
    if count != 0:
        return False
    
    return True