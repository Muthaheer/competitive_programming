from collections import defaultdict
class Tree:
    def __init__(self, v):
        self.v = v
        self.adj = defaultdict(list)
        self.s = [-1] * self.v

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def isBetweenBranchingNodes(self, node, branchingNodes):

        for i in self.adj[node]:
            if i not in branchingNodes:
                return False
        return True

    def assignS(self):
        availableNodes = set(range(self.v))
        
        while len(availableNodes) > 3:

            yes = 1
            toRemove = set()
            found = False
            branchingNodes = []
            
            for i in availableNodes:
                if len(self.adj[i]) > 2:
                    branchingNodes.append(i)

            for i in availableNodes:
                # non branching node? remove it and asign s
                if len(self.adj[i]) <= 2 and not self.isBetweenBranchingNodes(i, branchingNodes):
                    self.s[i] = yes
                    toRemove.add(i)
                    found = True

            

            availableNodes -= toRemove

            yes += 1

            if not found:
                break

        for i in availableNodes:
            self.s[i] = yes

        #print(self.s)

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
        print('Path: ')
        print(p)
        print(getInversionCount(p, len(p)))

solution()
    
    
    