def count_routers(houses, distance):
    routers = 1
    cur_house = houses[0]
    
    for house in houses:
        if house - cur_house >= distance:
            routers += 1
            cur_house = house
            
    return routers

def max_router_distance(houses, c):
    houses.sort()
    start = 1
    end = houses[-1] - houses[0]
    result = 0
    
    while start <= end:
        mid = (start + end) // 2
        if count_routers(houses, mid) >= c:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return result


N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

print(max_router_distance(houses, C))
