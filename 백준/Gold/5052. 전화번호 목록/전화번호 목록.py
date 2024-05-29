import sys
input = sys.stdin.readline

def is_consistent(phone_numbers):

    phone_numbers.sort()

    for i in range(len(phone_numbers) - 1):

        if phone_numbers[i+1].startswith(phone_numbers[i]):
            return "NO"
    return "YES"


t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    phone_numbers = [input().strip() for _ in range(n)]
    result = is_consistent(phone_numbers)
    results.append(result)

for result in results:
    print(result)