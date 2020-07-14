import random as rnd

class TreapNode():
    def __init__(self, x):
        self.x = x
        self.y = rnd.randrange(100)
        self.left = None
        self.right = None

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    #left - less than val
    #right - greater or equals to val
    def split(self, val):
        if (self.x < val):
            if (not self.right):
                return (self, None)

            l, r = self.right.split(val)
            self.right = l
            return (self, r)
        else:
            if (not self.left):
                return (None, self)

            l, r = self.left.split(val)
            self.left = r
            return (l, self)

    def __str__(self):
        return "{{x: {}, y: {}, left: {}, right: {}}}".format(self.x, self.y, self.left, self.right)

def mergeWithOneNode(leftOneNode, right):
    if (not right):
        return leftOneNode

    if (leftOneNode.x == right.x):
        if (leftOneNode.y >= right.y):
            leftOneNode.setRight(right)
            return leftOneNode
        else:
            right.setRight(mergeWithOneNode(leftOneNode, right.right))
            return right
    else:
        return merge(leftOneNode, right)

def merge(left, right):
    if (not left):
        return right

    if (not right):
        return left

    if (left.y > right.y):
        left.setRight(merge(left.right, right))
        return left
    else:
        right.setLeft(merge(left, right.left))
        return right


if __name__ == '__main__':
    root = TreapNode(2)

    for _ in range(10):
        node = TreapNode(2)
        l, r = root.split(node.x)
        root = merge(l, mergeWithOneNode(node, r))

    print(root)