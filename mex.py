# https://www.codechef.com/OCT17/problems/MEX

def solution(arr, n, k):
    mex = 0
    i = 0
    used = [0]*(n+k)

    while i < n:
        if arr[i] < n+k:
            used[arr[i]] = 1
        i += 1
    added = 0
    i = 0
    if k == 0:
        while i < (n+k) and used[i]:
            i += 1
    else:
        while added < k:
            if used[i] == 0:
                used[i] = 1
                added += 1
            i += 1
        while i < (n+k) and used[i]:
            i += 1

    print(i)

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))

    solution(arr, n, k)

    