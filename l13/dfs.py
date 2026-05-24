# class Graph:
#     def __init__(self, n):
#         self.n = n
#         self.adj = [[] for i in range(n)]

#     def createEdge(self, a, b):
#         self.adj(a - 1).append(b - 1)
#         self.adj(b - 1).append(a - 1)

#     def DFS(self, source):
#         visited = False * self.n
#         visited[source] = True

#         for node in self.adj[source]:
#             if not visited[node]:
#                 self.DFS(node, visited)

graph = {"a" : ["b", "c", "d"],
         "b" : ["e"],
         "c" : ["e", "d"],
         "d" : [], 
         "e" : []}

graph2 = {"a" : ["b", "e"],
          "b" : ["c", "d"],
          "c": ["d", "e"],
          "d" : ["e"],
          "e" : []}

visited = set()

def DFS(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for i in graph[root]:
            DFS(visited, graph, i)

# DFS(visited, graph, "a")
DFS(visited, graph2, "a")