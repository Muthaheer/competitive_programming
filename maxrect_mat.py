def largestRect(hist, n):
    stack = []
    maxRect = 0
    i = 0
    while i < n:
        if len(stack) == 0 or hist[i] >= hist[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            t = stack.pop()
            if len(stack):
                rectSize = hist[t] * (i - stack[-1] - 1)
            else:
                rectSize = hist[t] * i
            maxRect = max(rectSize, maxRect)

    while len(stack):
        t = stack.pop()
        if len(stack):
            rectSize = hist[t] * (i - stack[-1] - 1)
        else:
            rectSize = hist[t] * i
        maxRect = max(rectSize, maxRect)

    return maxRect

def maxRectArea(mat, rows, cols):
    dp = [0] * cols
    res = 0
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                dp[c] = 0
            else:
                dp[c] += 1
        res = max(res, largestRect(dp, cols))

    print(res)

mat = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
]
maxRectArea(mat, len(mat), len(mat[0]))