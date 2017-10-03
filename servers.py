from collections import defaultdict


class Graph:
    
    def __init__(self, v):
        self.v = v
        self.adj = defaultdict(list)

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def find(self, u, parent):
        if parent[u] == -1:
            return u
        else:
            return self.find(parent[u], parent)

    def union(self, u, v, parent):
        x = self.find(u, parent)
        y = self.find(v, parent)

        parent[x] = y

    # checks if this graph has a cycle
    def hasCycle(self):
        processed = set()
        parent = [-1] * self.v
        for i in range(self.v):
            for u in self.adj[i]:
                if (i, u) in processed:
                    continue
                x = self.find(i, parent)
                y = self.find(u, parent)

                if x == y:
                    return True
                else:
                    self.union(x, y, parent)
                processed.add((i, u))
                processed.add((u, i))

        return False

    # returns max number of vertices that can be included
    def dfs(self, u, visited):

        self.visited[u] = True
        for v in self.adj[u]:

            # check if visiting this node create a cycle
            
            if not visited[v]:
                self.dfs(v, visited)

    # returns maximum number vertices that can be connected
    # without exceeding the frequency-device count
    # and without forming a cycle
    def maxPairs(self, freqs, k):



def solution():
    g = Graph(3)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(0, 2)

    print(g.hasCycle())

solution()