
N = int(input())

cards = {}
for card in map(int, input().split()):
    cards[card] = 1

M = int(input())


results = []
for target in map(int, input().split()):
    if target in cards:
        results.append('1')
    else:
        results.append('0')

print(' '.join(results))
