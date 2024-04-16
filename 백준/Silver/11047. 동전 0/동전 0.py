def min_coins(N, K, coins):
    count = 0
    remaining = K

    for value in reversed(coins):
        if remaining == 0:
            break
        if value > remaining:
            continue
        count += remaining // value
        remaining %= value

    return count


N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

result = min_coins(N, K, coins)


print(result)