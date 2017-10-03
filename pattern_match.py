
# pattern: a-z, *, ?
# text: a-z
def isMatch(pattern, text):

    pLen = len(pattern)
    tLen = len(text)

    # we want to index from 1
    pattern = '$' + pattern
    text = '$' + text

    dp = [[False] * (pLen + 1) for i in range(tLen + 1)]

    dp[0][0] = True # empty string matches empty pattern

    # empty text matches only pattern: *, **, *** etc
    for i in range(1, pLen + 1):
        dp[0][i] = dp[0][i-1] and pattern[i] == '*'

    # non empty text never matches empty pattern
    for i in range(1, tLen + 1):
        dp[i][0] = False

    for i in range(1, tLen + 1):
        for j in range(1, pLen + 1):
            if text[i] == pattern[j] or pattern[j] == '?':
                dp[i][j] = True
            elif pattern[j] == '*':
                dp[i][j] = dp[i-1][j-1] | dp[i-1][j]
            else:
                dp[i][j] = False

    return dp[tLen][pLen]


print(isMatch('ab*d', 'abd'))
print(isMatch('ab*d', 'abbsdd'))
print(isMatch('ab*d', 'abds'))