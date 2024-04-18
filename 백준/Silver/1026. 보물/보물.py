n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()

s = 0
for i, j in  zip(a, b):
    s += (i * j)
print(s)