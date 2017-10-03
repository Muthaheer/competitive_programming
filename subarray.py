

def solution(par, arr, n):
    
    stack = []
    h = [-1]*n

    opposite = {i:j for i, j in zip('>})]', '<{([')}


    # print(opposite)

    for i,e in enumerate(par):
        if len(stack) and e in opposite and par[stack[-1]] == opposite[e]:
            # we've found largest index opening brace for e
            h[i] = stack.pop()
        else:
            stack.append(i)


    # print(stack, h)

    
    sums = [0]*n
    sums[0] = arr[0]
    for i in range(1, n):
        sums[i] = sums[i-1] + arr[i]

    sums.append(0)

    maxsum = [0]*n
    maxsum.append(0)
    ans = 0
    for i in range(n):
        if h[i] != -1 or not (i != 0 and h[i] == 0) :
            maxsum[i] = max(sums[i]-sums[h[i]-1]+maxsum[h[i]-1], maxsum[i])
        ans = max(ans, maxsum[i])

    print(ans)
    
t = int(input())
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    arr = list(map(int, input().strip().split(' ')))
    solution(s, arr, n)
