def knapsack(wt, val, n, W):
    # for the sake of easy implementation
    wt = [0] + wt
    val = [0] + val

    dp = [[0]*(W+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            if j >= wt[i]:
                dp[i][j] = max(dp[i-1][j], val[i]+dp[i-1][j-wt[i]])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[n][W])

knapsack([1,2,3], [6,10,12], 3, 5)