import random as rnd

class TreapNode():
    def __init__(self, listVal, maxSeqLen):
        self.listVal = listVal
        self.y = rnd.randrange(100000000)
        self.maxSeqLen = maxSeqLen
        self.subtreeMaxSeqLen = maxSeqLen
        self.left = None
        self.right = None

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def getLeftSubtreeMaxSeqLen(self):
        if (self.left):
            return self.left.subtreeMaxSeqLen
        return 0

    def getRightSubtreeMaxSeqLen(self):
        if (self.right):
            return self.right.subtreeMaxSeqLen
        return 0

    def updateSubtreeMaxSeqLen(self):
        self.subtreeMaxSeqLen = max(self.getLeftSubtreeMaxSeqLen(), self.getRightSubtreeMaxSeqLen(), self.maxSeqLen)

    #left - less than val
    #right - greater or equals to val
    def split(self, val):
        if (self.listVal < val):
            if (not self.right):
                return (self, None)

            l, r = self.right.split(val)
            self.right = l
            self.updateSubtreeMaxSeqLen()
            return (self, r)
        else:
            if (not self.left):
                return (None, self)

            l, r = self.left.split(val)
            self.left = r
            self.updateSubtreeMaxSeqLen()
            return (l, self)

    def findNodeAndUpdate(self, listVal, maxSeqLen):
        if (self.listVal == listVal):
            self.maxSeqLen = max(self.maxSeqLen, maxSeqLen)
            self.updateSubtreeMaxSeqLen()
            return self
        elif (self.listVal > listVal):
            if (self.left):
                foundNode = self.left.findNodeAndUpdate(listVal, maxSeqLen)
                if (foundNode):
                    self.updateSubtreeMaxSeqLen()
                return foundNode
            else:
                return None
        else:
            if (self.right):
                foundNode = self.right.findNodeAndUpdate(listVal, maxSeqLen)
                if (foundNode):
                    self.updateSubtreeMaxSeqLen()
                return foundNode
            else:
                return None

    def __str__(self):
        return "{{x: {}, y: {}, left: {}, right: {}}}".format(self.listVal, self.y, self.left, self.right)

def merge(left, right):
    if (not left):
        return right

    if (not right):
        return left

    if (left.y > right.y):
        left.setRight(merge(left.right, right))
        left.updateSubtreeMaxSeqLen()
        return left
    else:
        right.setLeft(merge(left, right.left))
        right.updateSubtreeMaxSeqLen()
        return right

def countMaxSeqLenArrayOpt(lst):
    maxSeqLen = [1 for _ in range(len(lst))]

    root = TreapNode(lst[0], 1)

    for i in range(1, len(lst)):
        l, r = root.split(lst[i])
        maxSeqLen[i] = 1 if (not l) else l.subtreeMaxSeqLen + 1
        if (r and r.findNodeAndUpdate(lst[i], maxSeqLen[i])):
            root = merge(l, r)
        else:
            root = merge(l, merge(TreapNode(lst[i], maxSeqLen[i]), r))

    return maxSeqLen

def countMaxSeqLenArrayTriv(lst):
    maxSeqLen = [1 for _ in range(len(lst))]

    for i in range(1, len(lst)):
        for j in range(i):
            if (lst[j] < lst[i]):
                maxSeqLen[i] = max(maxSeqLen[i], maxSeqLen[j] + 1)

    return maxSeqLen

if __name__ == '__main__':
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    maxSeqLenOpt = countMaxSeqLenArrayOpt(lst)
    print(max(maxSeqLenOpt))