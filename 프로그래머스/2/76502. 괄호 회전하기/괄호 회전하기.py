def is_valid(s):
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    return len(stack) == 0

def solution(s):
    answer = 0
    length = len(s)
    for i in range(length):
        rotated_s = s[i:] + s[:i]  # 왼쪽으로 i칸 회전한 문자열 생성
        if is_valid(rotated_s):
            answer += 1
    return answer