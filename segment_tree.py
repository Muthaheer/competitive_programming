class SegmentTree:

    def __init__(self, arr, n):
        self.arr = arr
        self.n = n
        self.size = 2*n - 1 # tree size
        self.tree = [0] * self.size

        self.constructTree(0, n-1, 0)
        # print(self.tree)


    def getMid(self, start, end):
        return start + (end - start) // 2

    def constructTree(self, start, end, i):
        if start == end:
            print(i)
            self.tree[i] = self.arr[start]
            return self.tree[i]
        elif end < start:
            return 0
        else:
            mid = self.getMid(start, end)
            self.tree[i] = self.constructTree(start, mid, 2*i+1) + self.constructTree(mid+1, end, 2*i+2)

            return self.tree[i]

    def getSum(self, start, end, i, qs, qe):
        if qs <= start and qe >= end:
            return self.tree[i]
        elif qs < start or qe > end:
            return 0
        else:
            return self.

    def getSum(self, start, end):
        self.getSumUtil(start, end)

s = SegmentTree([3,7,5,6,2], 5)