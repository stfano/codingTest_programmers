from collections import deque

def bfs(tree, start):
    queue = deque([(start, 0)])
    visited = set()
    max_distance = 0
    max_node = start

    while queue:
        node, dis = queue.popleft()
        visited.add(node)
        
        if dis > max_distance:
            max_distance = dis
            max_node = node
        
        for neighbor, weight in tree[node]:
            if neighbor not in visited:
                queue.append((neighbor, dis + weight))
                
    return max_node, max_distance

V = int(input())
tree = [[] for _ in range(V + 1)]


for _ in range(V):
    info = list(map(int, input().split()))
    node = info[0]
    edges = info[1:-1]
    for i in range(0, len(edges), 2):
        neighbor, weight = edges[i], edges[i+1]
        tree[node].append((neighbor, weight))

x, _ = bfs(tree, 1)
x1, y1 = bfs(tree, x)
print(y1)
