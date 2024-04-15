
n = int(input())

time = list(map(int, input().split()))

time.sort()

min_time = 0
all_time = 0

for t in time:
    min_time += t
    all_time += min_time


print(all_time)