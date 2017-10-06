# https://www.codechef.com/problems/CHFQUEUE
import math

def solution(arr, n, k):
    stack = []
    f = 1
    i = 0
    mod = 1000000007
    if k == 2:
        end = 0
        start = -1
        while i < n:
            # print(i, start, end)
            if arr[i] >= arr[end]:
                end = i
                if start == -1 or arr[i] > arr[start]:
                    start = i
            else:
                f *= math.factorial(end - start + 2) % mod
                start = -1
                end = i
            
            i += 1
            

        return f % mod

    while i < n:
        # print(i, stack)
        if len(stack) == 0 or arr[i] >= arr[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            t = stack.pop()
            f *= (i-t+1) % mod
        # print(i, stack)
        

    return f % mod



# arr = [2,1,2,1]
n, k = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))
print(solution(arr, n, k))