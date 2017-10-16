# https://www.codechef.com/OCT17/problems/CHEFCCYL

def getDistance(src, dest, cycle):
    n = cycle[0]
    if src == dest:
        return 0
    if src > dest:
        src, dest, = dest, src
    if src == dest - 1:
        return cycle[src]
    else:
        return cycle[dest]

def preprocess(n, cycles, outerCycle, outerCycleSum):

    # Calculate minDist for nodes of each cycle
    for i in range(n):
        thisCycleSum = sum(cycles[i][1:])

        for j in range(1, cycles[i][0]+1):
            cycles[i][j] = min(cycles[i][j], thisCycleSum-cycles[i][j])

    # for outer cycle, find min distance between the inner cycle making the outer cycle
    outerCycleMinDist = []
    totalWeight = outerCycleSum
    for i in range(n):
        for v1, v2, w in outerCycle:
            getDistance()

    print(cycles, outerCycle)
    print(getDistance(1, 2, cycles[1]))

def solution():
    n, q = list(map(int, input().split(' ')))
    cycles = []
    for _ in range(n):
        cycles.append(list(map(int, input().split(' '))))

    outerCycle = []
    outerCycleSum = 0
    for i in range(n):
        k = list(map(int, input().split(' ')))
        outerCycle.append(k)
        outerCycleSum += w

    preprocess(n, cycles, outerCycle, outerCycleSum)

solution()