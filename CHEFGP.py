# https://www.codechef.com/OCT17/problems/CHEFGP

def solution(s, x, y):
    n = len(s)
    counta = countb = 0
    for c in s:
        if c == 'a':
            counta += 1
        else:
            countb += 1
    curA = 0
    curB = 0
    res = ''
    totalLen = 0
    while totalLen < n:
        if counta > 0 and curA < x:
            res += 'a'
            counta -= 1
            curA += 1
            curB = 0
            totalLen += 1

        elif countb > 0 and curB < y:
            res += 'b'
            countb -= 1
            curB += 1
            curA = 0
            totalLen += 1
        
        else:
            res += '*'
            curA = curB = 0

        

    return res

def solution2(s, x, y):
    n = len(s)
    counta = countb = 0
    for c in s:
        if c == 'a':
            counta += 1
        else:
            countb += 1
    curA = 0
    curB = 0
    res = ''
    totalLen = 0
    turn = 0
    if counta < countb:
        turn = 1
    else:
        turn = 0
    while totalLen < n:
        if turn == 0 and counta > 0 and curA < x:
            res += 'a'
            counta -= 1
            curA += 1
            curB = 0
            totalLen += 1
            turn = 1

        elif turn == 1 and countb > 0 and curB < y:
            res += 'b'
            countb -= 1
            curB += 1
            curA = 0
            totalLen += 1
            turn = 0
        elif counta > 0 and curA < x:
            res += 'a'
            counta -= 1
            curA += 1
            curB = 0
            totalLen += 1
            turn = 1
        elif countb > 0 and curB < y:
            res += 'b'
            countb -= 1
            curB += 1
            curA = 0
            totalLen += 1
            turn = 0
        else:
            res += '*'
            curA = curB = 0

        if counta < countb:
            turn = 1
        else:
            turn = 0

        

    return res

# print(solution('aabb', 1, 2))
# print(solution('aaaaab', 2, 1))
# print(solution('aaaa', 1, 3))
t = int(input())
for _ in range(t):
    s = input()
    x, y = list(map(int, input().split(' ')))
    print(solution2(s,x,y))
    # print(solution(s,x,y))