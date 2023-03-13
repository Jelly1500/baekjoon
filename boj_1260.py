import sys
input = sys.stdin.readline

class Graph:
    def __init__(self, num_nodes):
        self.adj_list = {} # 인접 리스트 딕셔너리
        self.num_nodes = num_nodes # 노드 수
        self.visited = [0] * (num_nodes+1)
        for i in range(1, num_nodes + 1):
            self.adj_list[i] = [] # 각 노드에 대해 빈 리스트 할당
        
    def initVisit(self):
        for i in range(1, self.num_nodes + 1):
            self.visited[i] = 0

    def add_edge(self, u, v):
        self.adj_list[u].append(v) # u에서 v로 가는 엣지 추가
        self.adj_list[v].append(u) # v에서 u로 가는 엣지 추가(양방향 전용)
    
    def sort_nodes(self):
        for i in range(1, self.num_nodes+1):
            self.adj_list[i].sort()

    def DFS(self, start):
        self.visited[start] = 1
        print(start, end = " ")
        for i in self.adj_list[start]:
            if self.visited[i] == 0:
                self.visited[i] = 1
                self.DFS(i)
        return

    def BFS(self, start):
        if self.visited[start] == 0:
            self.visited[start] = 1
            print(start, end=" ")
        nextList = []
        for i in self.adj_list[start]:
            if self.visited[i] == 0:
                self.visited[i] = 1
                print(i, end=" ")
                nextList.append(i)
        for i in nextList:
            self.BFS(i)
        return
    
n,m,v = map(int, input().split())
graph = Graph(n)
for i in range(m):
    start, next = map(int, input().split())
    graph.add_edge(start, next)

graph.sort_nodes()
graph.DFS(v)
print()
graph.initVisit()
graph.BFS(v)
