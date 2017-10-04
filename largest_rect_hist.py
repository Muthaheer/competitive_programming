# http://www.geeksforgeeks.org/largest-rectangle-under-histogram/

def largestRect(hist, n):
    stack = []
    maxRect = 0
    i = 0
    while i < n:
        if len(stack) == 0 or hist[i] >= hist[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            t = stack.pop()
            if len(stack):
                rectSize = hist[t] * (i - stack[-1] - 1)
            else:
                rectSize = hist[t] * i
            maxRect = max(rectSize, maxRect)

    while len(stack):
        t = stack.pop()
        if len(stack):
            rectSize = hist[t] * (i - stack[-1] - 1)
        else:
            rectSize = hist[t] * i
        maxRect = max(rectSize, maxRect)

    print(maxRect)

largestRect([6, 2, 5, 4, 5, 1, 6], 7)