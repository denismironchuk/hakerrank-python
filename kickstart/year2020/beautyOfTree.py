class Node():
    def __init__(self, num, probA, probB):
        self.num = num
        self.children = []
        self.probA = probA
        self.probB = probB

        self.parentA = None
        self.parentB = None
        self.parent = None

    def addChild(self, child):
        self.children.append(child)

    def setParent(self, parent):
        self.parent = parent

    def setParentA(self, parent):
        self.parentA = parent

    def setParentB(self, parent):
        self.parentB = parent

def initParents(nodes, step, parentSetter):
    stack = []
    stack.append(nodes[1])

    processed = {}
    for node in nodes.values():
        processed[node.num] = False

    path = []

    while (stack):
        currNode = stack[-1]

        if (not processed[currNode.num]):
            processed[currNode.num] = True

            if (len(path) >= step):
                parentSetter(currNode, path[-step])

            path.append(currNode)

            for child in currNode.children:
                stack.append(child)
        else:
            stack.pop()
            path.pop()

def initParent(node, path, step, parentSetter):
    if (len(path) >= step):
        parentSetter(node, path[-step])

    path.append(node)

    for child in node.children:
        initParent(child, path, step, parentSetter)

    path.pop()

def initProbsNoRecur(nodes):
    stack = []
    processed = {}
    for node in nodes.values():
        processed[node.num] = False

    stack.append(nodes[1])

    while (stack):
        node = stack[-1]

        if (not processed[node.num]):
            processed[node.num] = True
            for child in node.children:
                stack.append(child)
        else:
            stack.pop()

            if (node.parentA):
                node.parentA.probA += node.probA

            if (node.parentB):
                node.parentB.probB += node.probB

def initProbabilities(node):
    for child in node.children:
        initProbabilities(child)

    if (node.parentA):
        node.parentA.probA += node.probA

    if (node.parentB):
        node.parentB.probB += node.probB

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n, a, b = map(int, input().split())

        parents = list(map(int, input().split()))

        nodes = {}

        for i in range(1, n + 1):
            nodes[i] = Node(i, 1 / n, 1 / n)

        for i in range(n - 1):
            parent = nodes[parents[i]]
            nodes[i + 2].setParent(parent)
            parent.addChild(nodes[i + 2])

        initParents(nodes, a, lambda node, parent: node.setParentA(parent))
        initParents(nodes, b, lambda node, parent: node.setParentB(parent))

        #initParent(nodes[1], [], a, lambda node, parent: node.setParentA(parent))
        #initParent(nodes[1], [], b, lambda node, parent: node.setParentB(parent))

        initProbsNoRecur(nodes)
        #initProbabilities(nodes[1])

        resultProb = 0

        for node in nodes.values():
            resultProb += node.probA + node.probB - (node.probA * node.probB)

        print("Case #{}: {:.6f}".format(t, resultProb))
