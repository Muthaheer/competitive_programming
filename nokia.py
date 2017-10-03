# from itertools import permutations
min = [0] * 51
for n in range(1, 51):
    min[n] = min[n//2] + min[n - n//2 - 1] + n+1

def solution2(n, m):
    global min
    max = n * (n+3) // 2
    if m < min[n]:
        print(-1)
    elif m <= max:
        print(0)
    else:
        print(m - max)


# brute force
# def solution(n, rem):
#     maxUsedLength = 0
#     for p in permutations(range(1, n+1)):
#         usedLength = 0
#         a = [0]*(n+2)
#         a[0] = a[n+1] = 1
        
#         for i in p:
#             # find 1 at left side
#             l = i-1
#             while l >= 0:
#                 if a[l] == 1:
#                     break
#                 l -= 1

#             r = i+1
#             while r < n+2:
#                 if a[r] == 1:
#                     break
#                 r += 1
            
#             usedLength += (i-l) + (r - i)
#             a[i] = 1

#         if usedLength <= rem and usedLength > maxUsedLength:
#             maxUsedLength = usedLength

#     if maxUsedLength == 0:
#         print(-1)
#     else:
#         print(rem - maxUsedLength)



# print(minRemaining(0, 5, 25))
# solution(2, 4)
# print(minRemaining(0,3,3))

t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split(' ')))
    solution2(n, m)