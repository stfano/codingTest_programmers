def min_num(sentence):
    # '-' 기준으로 식을 분할하여 각 부분을 리스트로 저장
    parts = sentence.split('-')
    # print(parts)
    # 첫 번째 파트를 계산 (여기에는 '-'가 없으므로 단순히 모든 수를 더함)
    first_part_sum = sum(map(int, parts[0].split('+')))
    # print(first_part_sum)
    # 나머지 파트들에서, 각각 '+'로 분할하여 수들을 더한 후, 전체 합에서 빼줌
    remaining_sum = sum(sum(map(int, part.split('+'))) for part in parts[1:])
    # print(remaining_sum)
    # 첫 번째 파트의 합에서 나머지 합을 뺀 값을 반환
    return first_part_sum - remaining_sum

sentence = input().strip()


print(min_num(sentence))
