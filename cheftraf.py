class Graph:
    def __init__(self, v):
        self.v = v
        self.g1 = [[float('inf')]*v for i in range(v)]
        self.g2 = [[float('inf')]*v for i in range(v)]

    def addEdge1(self, u, v, w):
        self.g1[u][v] = self.g1[v][u] = w

    def addEdge2(self, u, v, w):
        self.g2[u][v] = self.g2[v][u] = w

    def allPairShortest(self):

        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    if self.g1[i][j] > self.g1[i][k] + self.g1[k][j]:
                        self.g1[i][j] = self.g1[i][k] + self.g1[k][j]
                    if self.g2[i][j] > self.g2[i][k] + self.g2[k][j]:
                        self.g2[i][j] = self.g2[i][k] + self.g2[k][j]
        totalCost = 0
        for i in range(self.v):
            for j in range(i+1, self.v):
                totalCost += min(self.g1[i][j], self.g2[j][i])
        # print(self.g1)
        # print(self.g2)
        print(totalCost)


t = int(input())
for _ in range(t):
    n = int(input())
    g = Graph(n)

    for i in range(n-1):
        u, v, w = list(map(int, input().split(' ')))
        g.addEdge1(u-1, v-1, w)

    for i in range(n-1):
        u, v, w = list(map(int, input().split(' ')))
        g.addEdge2(u-1, v-1, w)

    g.allPairShortest()