from itertools import combinations

def solution(n, m):
    c = 0
    for p in combinations(range(1, n+1), 2):
        if sum(p) % m == 0:
            c += 1
            print(p)
    return c

def solution2(n, m):
    i = 1
    s = 0
    while i <= n:
        # try for each multiple of m
        k = m
        while k - i < i:
            k = k + m

        while k - i <= n:
            if k - i <= n and k - i >= 1 and k - i != i:
                s += 1
                # print(i, k-i)
            k += m
             
        # while True:
        #     if k - i < i:
        #         k += m
        #         continue
        #     if k - i <= n and k - i >= 1 and k - i != i:
        #         s += 1
        #         print(i, k-i)
        #         k += m
        #     else:
        #         break
        i += 1

    return s

t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split(' ')))
    # print(solution(n, m))
    print(solution2(n, m))