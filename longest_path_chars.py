# Solution for: https://discuss.codechef.com/questions/91826/medianet-recruitment-challenge-1

def dfs(mat, i, j, prevChar, visited, m, n):
    # if this is the first character in path, then skip checking prevChar
    # print('Args: ', i, j, prevChar)
    if i >= m or i < 0 or j >= n or j < 0:
        return 0
    elif prevChar and (ord(mat[i][j]) - ord(prevChar) != 1):
        # print('here', mat[i][j], prevChar)
        return 0
    elif (i, j) in visited:
        return visited[(i, j)]
    else:
        # print('working')
        visited[(i, j)] = max(
    dfs(mat, i-1, j-1, mat[i][j], visited, m, n) + 1,
    dfs(mat, i-1, j, mat[i][j], visited, m, n) + 1,
    dfs(mat, i-1, j+1, mat[i][j], visited, m, n) + 1,
    dfs(mat, i, j-1, mat[i][j], visited, m, n) + 1,
    dfs(mat, i, j+1, mat[i][j], visited, m, n) + 1,
    dfs(mat, i+1, j-1, mat[i][j], visited, m, n) + 1,
    dfs(mat, i+1, j, mat[i][j], visited, m, n) + 1,
    dfs(mat, i+1, j+1, mat[i][j], visited, m, n) + 1
    )
        return visited[(i, j)]

def solution(mat, m, n, startChar):
    # find the indices of starting char
    i = -1
    j = -1
    found = False
    for i in range(m):
        for j in range(n):
            if mat[i][j] == startChar:
                # print('hereeeee')
                found = True
                break
        if found:
            break                
    
    visited = {}

    return dfs(mat, i, j, None, visited, m, n) 

# mat = [['a', 'c', 'd'], ['h', 'b', 'e'], ['i', 'g', 'f']]
# print(solution(mat, 3, 3, 'e'))

# 2 4 4 a c d e h b a t i g f g j s e f f 3 3 a b c d e f g h i a

mat = [['a', 'c', 'd', 'e'], ['h', 'b', 'a', 't'], ['i', 'g', 'f', 'g'], ['j', 's', 'e', 'f']]
print(solution(mat, 4, 4, 'f'))