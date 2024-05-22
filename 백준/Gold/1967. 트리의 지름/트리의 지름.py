from collections import deque 


def bfs(tree, start):
    queue = deque([(start, 0)])
    vis = set()
    max = 0
    max_node = start

    while queue:
        node, dis = queue.popleft()
        vis.add(node)
        
        if dis > max :
            max = dis
            max_node = node
        for with_node, weight in tree[node]:
            if with_node not in vis:
                queue.append((with_node, dis + weight))
    return max_node, max

N = int(input())

tree = [[] for _ in range(N+1)]

for i in range(N - 1):
    infor = list(map(int, input().split()))
    node = infor[0]
    with_node, weight = infor[1], infor[2]
    tree[node].append((with_node, weight))
    tree[with_node].append((node, weight))

far_node, distance = bfs(tree, 1)
res_node, res_dis = bfs(tree, far_node)

print(res_dis)
