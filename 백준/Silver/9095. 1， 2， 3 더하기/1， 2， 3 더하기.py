def one_two_three_num(n):
    list = [0] * (n + 1)
    list[0] = 1

    for i in range(1, n + 1):
        for j in range(1, 4):
            if i - j >= 0:
                list[i] += list[i - j]
    return list[n]

T = int(input())
for _ in range(T):
    n = int(input())
    print(one_two_three_num(n))