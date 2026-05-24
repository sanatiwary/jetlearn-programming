from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, a, b):
        self.graph[a].append(b)
   
    def DFS(self, root):
        visited = set()
        if root not in visited:
            visited.add(root)
            for i in self.graph[root]:
                self.DFS(i)

        return visited
    
g = Graph()
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(3, 5)

print(g.DFS(0))