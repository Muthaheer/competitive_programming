# https://www.codechef.com/OCT17/problems/PERFCONT

def solution(probs, n, p):
    ck = 0
    hard = 0

    for pr in probs:
        # print('pr ', pr, p//2, p//10)
        if pr >= (p//2):
            ck += 1
        elif pr <= (p//10):
            hard += 1
    if ck == 1 and hard == 2:
        print('yes')
    else:
        print('no')

t = int(input())
for _ in range(t):
    n, p = list(map(int, input().split(' ')))
    probs = list(map(int, input().split(' ')))
    solution(probs, n, p)