# https://www.codechef.com/OCT17/problems/CHEFCOUN
import random
import math

def wrongSolver(a):
    n = len(a)
    mod = 2**32
    pref = [0]*n
    suf = [0]*n

    pref[0] = a[0]
    for i in range(1, n):
        pref[i] = (pref[i-1] + a[i]) % mod
    suf[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        suf[i] = (suf[i+1] + a[i]) % mod
    # print('wrong', pref)
    # print('wrong', suf)
    mn = (pref[0] + suf[0]) % mod
    where = 1
    for i in range(1, n):
        val = (pref[i] + suf[i]) % mod
        if val < mn:
            mn = val
            where = i + 1
    return where

def rightSolver(a):
    n = len(a)
    mod = 2**32
    pref = [0]*n
    suf = [0]*n

    pref[0] = a[0]
    for i in range(1, n):
        pref[i] = (pref[i-1] + a[i])
    suf[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        suf[i] = (suf[i+1] + a[i])
    # print('right', pref)
    # print('right', suf)
    mn = (pref[0] + suf[0])
    where = 1
    for i in range(1, n):
        val = (pref[i] + suf[i])
        if val < mn:
            mn = val
            where = i + 1
    return where

def tester(n):
    random.seed(64)
    arr = [0]*n
    # 99991 ≤ n ≤ 105, 1 ≤ ai ≤ 2 * 109
    # num = 2*(10**9)-n
   
    num =  294967295//n + n
    for i in range(n):
        # arr[i] = random.randint(2*(10**9)-n, 2*(10**9))
        arr[i] = num

    arr[0] = 2000000000
    # print(arr)
    # arr[n//2] = 2**32
    # print(arr)
    # print('Wrong solver', wrongSolver(arr))
    # print('Right solver', rightSolver(arr))
    w = wrongSolver(arr)
    r = rightSolver(arr)
    if w == r:
        print('Falied', n)

def generate(n):
    # arr = [0]*n
    # 99991 ≤ n ≤ 105, 1 ≤ ai ≤ 2 * 109
    # num = 2*(10**9)-n
    print(2000000000, end=' ')
    num =  294967295//n + n
    for i in range(1, n):
        print(num, end=' ')
    

    # arr[0] = 2000000000
    # print(*arr)


# n = int(input())
# tester(100023)
# for i in range(99991, 10**5):
#     tester(i)
t = int(input())
for _ in range(t):
    n = int(input())
    generate(n)
generate(10)
