
seq = [7, 2, 5, 3, 44, 5, 8, 99]

def findLIS(arr):
    n = len(arr)

    dp = [0] * n
    dp[1] = 1

    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    return max(dp)

print(findLIS(seq))