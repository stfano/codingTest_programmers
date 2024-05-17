from collections import deque

def bfs(tree, start):
    queue = deque([(start,0)])
    visited = set()
    max = 0
    max_node = start
    
    while queue:
        node, dis = queue.popleft()
        visited.add(node)
        
        if dis > max :
            max = dis
            max_node = node
        
        for with_node, distance in tree[node]:
            if with_node not in visited:
                queue.append((with_node, dis + distance))
                
    return max_node, max

N =  int(input())

tree = [[] for _ in range(N + 1)]

for _ in range(N):
    information = list(map(int, input().split()))
    node = information[0]
    edges = information[1:-1]
    for i in range(0,len(edges), 2): # 0, 2, 2
        with_node, weight = edges[i], edges[i+1]
        tree[node].append((with_node, weight))
        
node1, distance1 = bfs(tree, 1)
far_node, far_dis = bfs(tree, node1)
print(far_dis)