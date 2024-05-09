from collections import deque

M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(queue, si, sj):


    while queue:
        x, y = queue.popleft()
        for dx, dy in ((0,1), (0,-1),(1,0),(-1,0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))

queue = deque([])
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i,j))
            
bfs(queue, i, j)
            
max_day = 0
for row in arr:
    if 0 in row:
        print(-1)
        break
    max_day = max(max_day, max(row))
else :
    print(max_day - 1)