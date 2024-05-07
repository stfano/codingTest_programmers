def bfs(si, sj):
    queue = [(si, sj)]
    visited[si][sj] = 1  # 새로운 단지의 첫 집이므로 방문 처리
    cnt = 1  # 단지 안 집의 개수 반환을 위한 cnt

    while queue:  # 큐가 비어있을 때까지 반복 진행
        xi, xy = queue.pop(0)

        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx, ny = xi + dx, xy + dy

            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                # 정사각형 범위를 만족하면서, 현재 좌표에 집이 있어야 하고, 방문하지 않은 집이어야 함
                queue.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]  # 다 0으로 채운 다음 방문하면 1로 바꾸기
answer = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:  # 방문하지 않았고 집이 있으면 순회하기
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for count in answer:
    print(count)
