from collections import defaultdict
def solution(arr, n):

    # dp = [[0]*n for i in range(n)]
    dp = defaultdict(int)
    s = 0
    for i in range(n):
        # dp[i][i] = arr[i]
        # s += dp[i][i]
        dp[(i, i)] = arr[i]
        s += arr[i]

    for i in range(n-2+1):
        j = i + 2 - 1
        # dp[i][j] = arr[i] & arr[j]
        # s += dp[i][j]
        dp[(i, j)] = arr[i] & arr[j]
        s += dp[(i, j)]
    
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            # dp[i][j] = dp[i][i] & dp[i+1][j-1] & dp[j][j]
            dp[(i, j)] = arr[i] & dp[(i+1,j-1)] & arr[j]
            if dp[(i, j)] == 0:
                break
            s += dp[(i, j)]

    return s

def solution2(arr, n):
    

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    print(solution(arr, n))