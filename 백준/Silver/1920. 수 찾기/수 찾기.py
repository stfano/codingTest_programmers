n_a = int(input())
a = list(map(int, input().split()))

# 리스트 a를 집합으로 변환하여 빠른 검색을 가능하게 함
a_set = set(a)

n_b = int(input())
b = list(map(int, input().split()))

# 리스트 b의 각 요소에 대해 집합 a_set에서 존재 여부를 확인
for i in b:
    if i in a_set:
        print("1")
    else:
        print("0")
