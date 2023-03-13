class Node:
    def __init__(self, next):
        self.next = next

s = []
visited = [0] * 1001

def dfs(nodes, v):
    s.append(v)
    visited[v] = 1
    if len(nodes[v]) == 0:
        return
    for i in nodes[v]:
        if not visited[i.next]:
            visited[i.next] = 1
            
            dfs(nodes, i.next)

        
n, m, v = map(int, input().split())
nodes = [[] for i in range(n+1)]
for i in range(m):
    start, next = map(int, input().split())
    nodes[start].append(Node(next))

dfs(nodes, v)
print(s)