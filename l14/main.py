class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(v)]

    def DFS(self, temp, x, visited):
        visited[x] = True
        temp.append(x)

        for i in self.adj[x]:
            if not visited[i]:
                temp = self.DFS(temp, i, visited)

        return temp
    
    def addEdge(self, a, b):
        self.adj[a].append(b)
        self.adj[b].append(a)

    def connectedNodes(self):
        visited = []
        connected = []

        for i in range(self.v):
            visited.append(False)

        for a in range(self.v):
            if not visited[a]:
                temp = []
                connected.append(self.DFS(temp, a, visited))

        return connected

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(2, 1)
g.addEdge(4, 3)

print(g.connectedNodes())
