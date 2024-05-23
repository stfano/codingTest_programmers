N = int(input())
infor = list(map(int, input().split()))
delnode = int(input())

def bfs(infor, delnode):
    infor[delnode] = -2 # 제거할 노드 -2 로 표시 
    
    for i in range(len(infor)): # 전체 트리 돌기 
        if infor[i] == delnode: # 자식노드가 있다면 
            bfs(infor, i) # 다시 재귀를 통해서 삭제 

bfs(infor, delnode)
count = 0
for _ in range(len(infor)): # 다시 전체 트리 돌면서
    if infor[_] != -2 and _ not in infor: # 제거되지않은 노드여야하고, 부모노드가 있지 않아야 한다. 
        count += 1 
print(count)