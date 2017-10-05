class FenwickTree:

    def __init__(self, arr, n):
        self.arr = arr
        self.n = n
        self.tree = [0] * (n+1)

        for i in range(n):
            self.updateVal(i, self.arr[i])

        print(self.tree)

    def updateVal(self, index, val):
        index += 1 # we have a dummy node at 0
        while index > 0:
            self.tree[index] += val
            index = index - (index & (-index))
    
    def getSum(self, index):
        index += 1
        res = 0
        while index <= self.n:
            res += self.tree[index]
            index = index + (index & (-index))

        return res

arr = [1,4,8,3,5,6,2]
t = FenwickTree(arr, len(arr))
print(t.getSum(3))
print(t.updateVal(3, 2))
print(t.getSum(3))