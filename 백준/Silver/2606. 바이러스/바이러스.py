def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 입력 받기
n = int(input())  # 컴퓨터의 수
m = int(input())  # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

# 그래프 생성
graph = {}
for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 웜 바이러스 전파 확인
visited = set()
dfs(graph, 1, visited)

# 1번 컴퓨터를 제외한 방문한 컴퓨터의 수 출력
print(len(visited) - 1)
