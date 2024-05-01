from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maze, start, end):
    n, m = len(maze), len(maze[0])
    visited = [[False] * m for _ in range(n)] 
    queue = deque([start]) 
    visited[start[0]][start[1]] = True 
    distance = 1 

    while queue:
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()
            if (x, y) == end: 
                return distance
            for i in range(4): 
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        distance += 1 


n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]


start = (0, 0)
end = (n-1, m-1)

result = bfs(maze, start, end)
print(result)
