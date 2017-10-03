from collections import defaultdict

dp = {}
def dfs(g, src, depth, weight):
    global dp
    if weight == 0 and depth == 0:
        return 1
    elif weight < 0 or depth < 0:
        return 0
    else:
        key = (src, depth, weight)
        if key in dp:
            #print('dp')
            return dp[key]
        c = 0
        for i in range(10):
            c += dfs(g, i, depth - 1, weight - g[src][i])
        dp[key] = c
        return c

def solution(n, w):
    global count
    global paths
    mod = 1000007
    g = defaultdict(defaultdict)
	
    for i in range(10):
        for j in range(10):
            g[i][j] = abs(i-j)
    count = 0
    
    for i in range(1, 10):
        count += dfs(g, i, n-1, w) % mod

    #print(dp)


    return count % mod

t = int(input())
for _ in range(t):
	n, w = list(map(int, input().split(' ')))
	print(solution(n, w))

