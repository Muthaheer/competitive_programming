from collections import defaultdict
class Tree:
    def __init__(self, v):
        self.v = v
        self.adj = defaultdict(list)
        self.s = [-1] * self.v
        self.degree = [0] * self.v

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.degree[u] += 1
        self.degree[v] += 1

    def isBetweenBranchingNodes(self, node, branchingNodes):
        if self.degree[node] <= 1:
            return False
        for i in self.adj[node]:
            if i not in branchingNodes:
                
                return False

        # print('Between branch', node, branchingNodes, self.adj[node])
        return True

    # calculates S values for all nodes
    def assignS(self):

        # nodes for which S is yet to be calculated
        availableNodes = set(range(self.v))
        
        # lets do it until we have something to calculate
        while len(availableNodes):

            yes = 1
            toRemove = set()
            found = False
            branchingNodes = []

            # find branching nodes ? maybe this can be removed
            for i in availableNodes:
                if self.degree[i] > 2:
                    branchingNodes.append(i)

            for i in availableNodes:
                # non branching node? remove it and asign s
                
                if self.degree[i] <= 2 and self.degree[i] >= 0 and not self.isBetweenBranchingNodes(i, branchingNodes):
                    self.s[i] = yes
                    toRemove.add(i)

                    self.degree[i] = 0

                    for a in self.adj[i]:
                        if self.degree[a] > 0 and self.degree[a] <= 2:
                            self.degree[a] -= 1

                    found = True

            

            availableNodes -= toRemove

            yes += 1

            if not found:
                break
        # print('Rem: ', availableNodes)
        for i in availableNodes:
            self.s[i] = yes

        # print(self.degree, self.s)

        #print(self.s)

    # returns dfs to v in path, return True if path is found
    def dfs(self, u, v, visited, path):
        visited[u] = True
        if u == v:
            path.append(self.s[u])
            #path.append(u)
            return True
        for i in self.adj[u]:
            if not visited[i]:
                visited[i] = True
                if self.dfs(i, v, visited, path):
                    path.append(self.s[u])
                    #path.append(u)
                    return True
        return False

    # returns path mapped to S values
    def getSPath(self, u, v):
        path = []
        visited = [False] * self.v
        self.dfs(u, v, visited, path)
        return path[::-1]

def getInversionCount(arr, n):
    c = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                c += 1
    return c

    
def solution():
    n, q = list(map(int, input().split(' ')))
    t = Tree(n)

    for i in range(n-1):
        u, v = list(map(int, input().split(' ')))
        t.addEdge(u-1, v-1)
    #print(t.adj)
    t.assignS()

    for i in range(q):
        u, v = list(map(int, input().split(' ')))
        p = t.getSPath(u-1, v-1)
        # print('Path: ')
        # print(p)
        print(getInversionCount(p, len(p)))

t = int(input())
for _ in range(t):
    solution()
    
    
    