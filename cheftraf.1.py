from collections import defaultdict
import heapq

class Graph:
    def __init__(self, v):
        self.v = v
        self.g1 = defaultdict(list)
        self.g2 = defaultdict(list)

    def addEdge1(self, u, v, w):
        self.g1[u].append((v, w))
        self.g1[v].append((u, w))

    def addEdge2(self, u, v, w):
        self.g2[u].append((v, w))
        self.g1[v].append((v, w))

    def djikstra(self, src):
        visited = [False] * self.v
        h = [] # heap
        distMap = {} # map of vertex  (distance, vertex) tuple

        # for src
        d = (0, src)
        distMap[src] = d
        h.append(d)
        for i in range(self.v):
            if i != src:
                d = (float('inf'), 0)
                distMap[i] = d
                h.append(d)
        heapq.heapify(h)

        while len(h):
            distAndVertex = heapq.heappop()
            dist = distMap[u]

            for v, w in self.g1[u]:
                if w < dist[0]:
                    dist[0] = w


    def allPairShortest(self):
        print(self.g1)
        print(self.g2)
        # for k in range(self.v - 1):
        #     for i in range(self.v):
        #         for j in range(self.v):
        #             if self.g1[i][j] > self.g1[i][k] + self.g1[k][j]:
        #                 self.g1[i][j] = self.g1[i][k] + self.g1[k][j]
        #             if self.g2[i][j] > self.g2[i][k] + self.g2[k][j]:
        #                 self.g2[i][j] = self.g2[i][k] + self.g2[k][j]
        
                    
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