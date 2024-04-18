change_money = [500, 100, 50, 10, 5, 1]

moeny = int(input())

count = 0

remain = 1000 - moeny

for i in change_money:
    if remain >= i: # 380 >= 500 , 100
        count = count + remain // i
        remain = remain % i

print(count)