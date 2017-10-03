# https://www.codechef.com/problems/LAPIN
from collections import defaultdict

def isPerm(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    if n1 != n2:
        return False
    else:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for i in str1:
            freq1[i] += 1

        for i in str2:
            freq2[i] += 1

        for i in str1:
            if freq1[i] != freq2[i]:
                return False
        return True

def solution(str1, n):
    if n % 2 == 0:
        if isPerm(str1[0:n//2], str1[n//2:]):
            print('YES')
        else:
            print('NO')
    else:
        if isPerm(str1[0:n//2], str1[n//2+1:]):
            print('YES')
        else:
            print('NO')

t = int(input())
for _ in range(t):
    s = input()
    solution(s, len(s))