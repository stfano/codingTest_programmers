N = int(input())

tree = {}
for i in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def pre(root):
    if root != '.':
        print(root, end='')
        pre(tree[root][0])
        pre(tree[root][1])
    
def between(root):
    if root != '.':
        between(tree[root][0])  # left
        print(root, end='')  # root
        between(tree[root][1])  # right

def back(root):
    if root != '.':
        back(tree[root][0])  # left
        back(tree[root][1])  # right
        print(root, end='')  # root
        
pre('A')
print()
between('A')
print()
back('A')