# https://www.codechef.com/problems/CONFLIP

def solution(n, istate, which):
    if n % 2 == 0:
        return n//2
    else:
        if istate == which:
            return n//2
        else:
            return n - n//2

t = int(input())
for _ in range(t):
    g = int(input())
    for i in range(g):
        init, n, which = list(map(int, input().split(' ')))
        print(solution(n, init, which)) 