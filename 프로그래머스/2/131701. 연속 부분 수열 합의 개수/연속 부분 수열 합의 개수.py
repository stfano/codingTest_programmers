def solution(elements):
    n = len(elements)
    
    result = []
    

    extended_elements = elements + elements
    # print(extended_elements)
    # 모든 시작 위치에서 모든 길이의 연속 부분 수열의 합을 구합니다.
    for start in range(n):
        for length in range(1, n+1):
            # 현재 시작 위치부터 길이가 length인 부분 수열의 합을 구합니다.
            sub_sum = sum(extended_elements[start:start+length])
            result.append(sub_sum)
    
    # print(set(result))
    # 모든 부분 수열의 합을 구했으므로 중복을 제거한 후 결과를 반환합니다.
    return len(set(result))