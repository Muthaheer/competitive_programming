from itertools import permutations
n = [1,2,3,4,5,6]
perms = []
for p in permutations(n, 6):
    valid = True
    for i, e in enumerate(p):
        if e == i + 1 or (p[e-1] != (i+1)):
            valid = False
            break
    if valid:
        # print(p)
        perms.append(p)
# print(len(perms))

def solution(arr, n):
    global perms

    adj = [set() for i in range(7)]
    for i in range(1, n):
        if arr[i-1] == arr[i]:
            return [-1]
        adj[arr[i-1]].add(arr[i])
        adj[arr[i]].add(arr[i-1])

    for p in perms:
        valid = True
        for i, e in enumerate(p):
            index = i + 1
            if index in adj[e] or e in adj[index]:
                valid = False
                break
        if valid:
            return p

    return [-1]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    print(*solution(arr, n))