n = int(input())
p_card = list(map(int, input().split()))

card_count = {}
for card in p_card:
    if card in card_count:
        card_count[card] += 1
    else:
        card_count[card] = 1

m = int(input())
c_card = list(map(int, input().split()))

results = []
for ccard in c_card:
    if ccard in card_count:
        results.append(str(card_count[ccard]))
    else:
        results.append("0")

print(" ".join(results))

