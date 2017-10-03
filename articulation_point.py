from collections import defaultdict

WHITE = 0 # yet to process
GRAY = 1 # processing
BLACK = 2 # processed

class Graph:
    
    def __init__(self, v):
        self.adj = defaultdict(list)
        self.color = [WHITE] * self.v

    def addEdge(u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
        

    def dfs(self, u):
        self.color[u] = GRAY
        
        for v in self.adj[u]:
            if self.color[v] == WHITE:
                # this is a tree edge
                self.dfs(v)
            elif self.color[v] == GRAY:
                # this is a back edge
                pass
            else:
                # this is a forward/cross edge
                pass

        self.color[u] = BLACK