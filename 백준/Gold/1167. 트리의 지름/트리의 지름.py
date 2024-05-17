from collections import defaultdict

def find_farthest_node(tree, start):
    visited = set()
    stack = [(start, 0)]  
    farthest_node = start
    max_distance = 0

    while stack:
        node, distance = stack.pop()
        visited.add(node)

        if distance > max_distance:
            max_distance = distance
            farthest_node = node

        for neighbor, weight in tree[node]:
            if neighbor not in visited:
                stack.append((neighbor, distance + weight))

    return farthest_node, max_distance

def tree_diameter(tree):

    node1, _ = find_farthest_node(tree, 1)

    _, diameter = find_farthest_node(tree, node1)
    return diameter

def main():

    V = int(input())
    tree = defaultdict(list)


    for _ in range(V):
        info = list(map(int, input().split()))
        node = info[0]
        edges = info[1:-1]
        for i in range(0, len(edges), 2):
            neighbor, weight = edges[i], edges[i+1]
            tree[node].append((neighbor, weight))

    print(tree_diameter(tree))

if __name__ == "__main__":
    main()
