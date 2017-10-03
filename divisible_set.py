
def sortByDivisibility(arr):

    print(sorted(arr, cmp=lambda x, y: 1 if x % y == 0 else -1))

def getMaxDivisionSet(arr):
    n = len(arr)
    
    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        for j in range(0, i):
            if (arr[i] % arr[j] == 0 or arr[j] % arr[i] == 0) and (dp[j] + 1 > dp[i]):
                dp[i] = dp[j] + 1

    print(dp)


getMaxDivisionSet([2, 4, 6, 12, 7])
getMaxDivisionSet([4,2,8,24,6])

