
def minCutsPalindrome(string):
    n = len(string)

    # dp for palindrome. pal[i][j] is true if string[i] to string[j] is a palindrome
    pal = [[False]*n for i in range(n)] 
    for i in range(n):
        pal[i][i] = True
    
    # dp for mincuts. cuts[i][j] stores minimum cuts needed for string[i] to string[j]
    cuts = [[float('inf')]*n for i in range(n)]

    # calculate pal and cuts for substrings of length k in bottom up fashion
    for k in range(2, n+1):
        for i in range(0, n-k+1):
            j = i + k - 1

            if k == 2:
                pal[i][j] = string[i] == string[j]
            else:
                pal[i][j] = (string[i] == string[j]) and pal[i+1][j-1]

            if pal[i][j]:
                cuts[i][j] = 0
            else:
                for c in range(i, j):
                    cuts[i][j] = min(cuts[i][j], cuts[i][c] + cuts[c+1][j] + 1)

    return cuts[0][n-1]

print(minCutsPalindrome('ababbbabbababa'))