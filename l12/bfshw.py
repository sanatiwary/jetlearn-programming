class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] * n for i in range(n)]

    def createEdge(self, a, b):
        self.adj[a - 1].append(b - 1)
        self.adj[b - 1].append(a - 1)

    def BFS(self, source):
        visited = [False] * self.n
        dist = [-1] * self.n
        results = []

        next = []
        next.append(source)
        visited[source] = True
        dist[source] = 0

        while next:
            s = next.pop(0)
            results.append(s)

            for node in self.adj[s]:
                if not visited[node]:
                    next.append(node)
                    visited[node] = True
                    dist[node] = dist[s] + 1

        return dist
    
graph = Graph(4)
graph.createEdge(1, 2)
graph.createEdge(1, 3)
graph.createEdge(2, 4)

print(graph.BFS(0))
print(graph.BFS(1))
print(graph.BFS(2))