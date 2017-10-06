# Solution for http://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
from collections import deque
def printMaxK(arr, n, k):

    # stores elements in decreasing order from q[0] to q[-1]
    q = deque()

    i = 0
    while i < k:
        # remove elements from deque that are lesser than current elem
        # cuz they are useless
        while len(q) and arr[q[-1]] <= arr[i]:
            q.pop()

        q.append(i)
        i += 1

    while i < n:
        print(arr[q[0]])
        # remove all elements that are out of this window
        while len(q) and q[0] <= i - k:
            q.popleft()

        # now remove elements that are useless, i.e they are smaller
        while len(q) and arr[q[-1]] <= arr[i]:
            q.pop()

        q.append(i)
        i += 1


    print(arr[q[0]])

# arr = [1,2,3,1,4,5,2,3,6]
# printMaxK(arr, len(arr), 3)
arr = [1,8,3,4]
printMaxK(arr, len(arr), 2)