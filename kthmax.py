def solution():
    n, k = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))
    subs = []
    arr.sort(reverse=True)
    subs.append(arr[0])

    for l in range(n-1, 0, -1):
        for i in range(n-l+1):
            subs.append(arr[i])

    for q in range(k):
        i = int(input())
        print(subs[i-1])

def solution2():
    n, k = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))
    subs = []

    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i + l
            f = arr[i:j]
            # f.sort(reverse=True)
            subs.append(f)

    subs.sort(reverse=True)

    print(subs)

    for q in range(k):
        i = int(input())
        print(subs[i-1][0])

t = int(input())
for _ in range(t):
    solution2()