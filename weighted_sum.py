from collections import defaultdict

count = 0

def dfs(g, src, depth, weight):
    global count
    if weight == 0 and depth == 0:
        count += 1
    elif weight < 0 or depth < 0:
        return
    else:
        for i in range(10):
            dfs(g, i, depth - 1, weight - g[src][i])

def solution(n, w):
    global count
    global paths
    g = defaultdict(defaultdict)
	
    for i in range(10):
        for j in range(10):
            g[i][j] = abs(i-j)
    count = 0
    for i in range(1, 10):
        dfs(g, i, n-1, w)


    return count

t = int(input())
for _ in range(t):
	n, w = list(map(int, input().split(' ')))
	print(solution(n, w))

