# https://www.codechef.com/problems/CHSQARR
from collections import deque
def computeMaxColHelper(arr, n, k):

    # stores elements in decreasing order from q[0] to q[-1]
    q = deque()
    res = []
    i = 0
    while i < k:
        # remove elements from deque that are lesser than current elem
        # cuz they are useless
        while len(q) and arr[q[-1]] <= arr[i]:
            q.pop()

        q.append(i)
        i += 1

    while i < n:
        # print(arr[q[0]])
        res.append(arr[q[0]])
        # remove all elements that are out of this window
        while len(q) and q[0] <= i - k:
            q.popleft()

        # now remove elements that are useless, i.e they are smaller
        while len(q) and arr[q[-1]] <= arr[i]:
            q.pop()

        q.append(i)
        i += 1

    res.append(arr[q[0]])

    return res

def computeMaxCol(arr, rows, cols, colLen):
    maxCol = []
    for i in range(rows):
        maxCol.append(computeMaxColHelper(arr[i], cols, colLen))
    return maxCol

def computeMaxMatHelper(arr, col, n, k):
    # stores elements in decreasing order from q[0] to q[-1]
    # print('here')
    q = deque()
    res = []
    i = 0
    while i < k:
        # remove elements from deque that are lesser than current elem
        # cuz they are useless
        while len(q) and arr[q[-1]][col] <= arr[i][col]:
            q.pop()

        q.append(i)
        i += 1

    while i < n:
        # print('lol')
        # print(arr[q[0]])
        res.append(arr[q[0]][col])
        # remove all elements that are out of this window
        while len(q) and q[0] <= i - k:
            q.popleft()

        # now remove elements that are useless, i.e they are smaller
        while len(q) and arr[q[-1]][col] <= arr[i][col]:
            q.pop()

        q.append(i)
        i += 1

    res.append(arr[q[0]][col])

    return res

# def computeMaxMat(maxCols, rows, cols, a):
#     maxMat = []
#     for col in range(cols):
#         maxMat.append(computeMaxMatHelper(maxCols, col, rows, a))

#     return maxMat

def computeMaxMat(rows, cols, a, b):
    global arr

    maxMat = []
    if rows == 1:
        # compute only maxRows
        for row in range(rows):
            maxMat.append(computeMaxColHelper(arr, cols, b))
    elif cols == 1:
        # compute only maxCols
        for col in range(cols):
            maxMat.append(computeMaxMatHelper(arr, col, rows, a))
    else:
        # compute both
        maxCols = []
        for row in range(rows):
            maxCols.append(computeMaxColHelper(arr[row], cols, b))
        # print(maxCols)
        for col in range(len(maxCols[0])):
            maxMat.append(computeMaxMatHelper(maxCols, col, len(maxCols), a))

    return maxMat

def partialSum(arr, rows, cols):
    psum = [[0 for j in range(cols+1)] for i in range(rows+1)]
    psum[0][0] = arr[0][0]
    for i in range(1, cols):
        psum[0][i] += psum[0][i-1] + arr[0][i]

    for i in range(1, rows):
        psum[i][0] += psum[i-1][0] + arr[i][0]

    for i in range(1, rows):
        for j in range(1, cols):
            psum[i][j] = psum[i-1][j] + psum[i][j-1] + arr[i][j] - psum[i-1][j-1]

    return psum




def precompute(arr, r, c):
    global maxMat, rows, cols, psum
    rows, cols = r, c

    psum = partialSum(arr, rows, cols)

def getSum(endR, endC, a, b):
    global psum
    startR, startC = endR - a + 1, endC - b + 1
    s = psum[endR][endC] - psum[endR][startC-1] - psum[startR-1][endC] + psum[startR-1][startC-1]
    # print('return s at', endR, endC, 'as', s)
    return s

def query(a, b):
    global rows, cols, psum, maxMat
    if a == 1 and b == 1:
        print(0)
        return
    maxMat = computeMaxMat(rows, cols, a, b)
    # print(maxMat)
    minOps = float('inf')
    for j in range(cols-b+1):
        for i in range(rows-a+1):
            # print('jay', i, j)
            orgr, orgc = i+a-1, j+b-1
            sumHere = getSum(orgr, orgc, a, b)
            # print(j, i)
            maxHere = maxMat[j][i]
            # print('maxHere', maxHere)
            opsHere = a*b*maxHere - sumHere
            minOps = min(minOps, opsHere)

    print(minOps)


# arr = [
#     [1, 8, 3, 4],
#     [5, 2, 3, 1],
#     [3, 6, 2, 2]
# ]

r, c = list(map(int, input().split(' ')))
arr = []
for i in range(r):
    arr.append(list(map(int, input().split(' '))))
precompute(arr, r, c)
q = int(input())
for _ in range(q):
    a, b = list(map(int, input().split(' ')))
    query(a,b)