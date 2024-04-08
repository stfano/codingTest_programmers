def solution(k, tangerine):
    # 각 귤의 크기별 카운트를 저장할 딕셔너리 생성
    counts = {}
    for size in tangerine:
        counts[size] = counts.get(size, 0) + 1
    
    # 딕셔너리의 값들을 내림차순으로 정렬하여 리스트로 변환
    sorted_counts = sorted(counts.values(), reverse=True)
    
    # k만큼 빼면서 카운트를 증가시키고, 카운트가 음수가 되면 중단
    diff = 0
    for count in sorted_counts:
        k -= count
        diff += 1
        if k <= 0:
            break
    
    return diff