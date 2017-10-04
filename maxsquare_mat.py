def maxSquare(mat, rows, cols):
    s = [[0]*cols for i in range(rows)]

    for i in range(rows):
        s[i][0] = mat[i][0]

    for i in range(cols):
        s[0][i] = mat[0][i]
    res = 0
    for i in range(1, rows):
        for j in range(1, cols):
            if mat[i][j] == 1:
                s[i][j] = min(s[i-1][j], s[i][j-1], s[i-1][j-1])+1
            else:
                s[i][j] = 0
            res = max(res, s[i][j])

    return res

m = [
        [0, 1, 1, 0, 1], 
        [1, 1, 0, 1, 0], 
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]

print(maxSquare(m, 6, 5))