def bfs(si, sj):
    queue = []
    queue.append((si, sj))
    visited[si][sj] = 1 
    cnt = 1 
    
    while queue: 
        xi, xy = queue.pop(0)
        for dx, dy in ((-1,0), (1,0), (0,1), (0,-1)):
            nx, ny = xi+dx, xy+dy
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    
    answer = []
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and visited[i][j] == 0:
                answer.append(bfs(i, j))
    
    print(len(answer))
