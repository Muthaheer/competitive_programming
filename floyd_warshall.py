class Graph:
    
    def __init__(self, v):
        self.v = v
        self.adj = [[float('inf')] * self.v for i in range(self.v)]
        for i in range(v):
            self.adj[i][i] = 0

    def addEdge(self, u, v, w):
        self.adj[u][v] = w

    def printPath(self, src, dest, pathMat):
        if src == dest:
            print(dest)
        elif src == float('inf'):
            print('X')
            return
        else:
            print(src, '-->', end='')
            self.printPath(pathMat[src][dest], dest, pathMat)

    def printAllPaths(self, pathMat):
        for i in range(self.v):
            for j in range(self.v):
                if i != j:
                    print('Path ', i, 'to', j, ':  ')
                    self.printPath(i, j, pathMat)
    
    def floydWarshall(self):

        dist = [[self.adj[i][j] for j in range(self.v)] for i in range(self.v) ]
        path = [[float('inf') for j in range(self.v)] for i in range(self.v)]

        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        if i == 0 and j == 3 and k == 2:
                            print('hey ', dist)
                            print('hey ', dist[i][k] + dist[k][j])
                        dist[i][j] = dist[i][k] + dist[k][j]
                        path[i][j] = k
                    else:
                        if dist[i][j] != float('inf') and path[i][j] == float('inf'):
                            path[i][j] = j
        print(path)
        self.printAllPaths(path)
        
        return dist


def solution():
    g = Graph(4)
    g.addEdge(0, 3, 10)
    g.addEdge(0, 1, 5)
    g.addEdge(1, 2, 3)
    g.addEdge(2, 3, 1)

    print(g.floydWarshall())

solution()