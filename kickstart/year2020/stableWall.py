from collections import deque

class Node():
    def __init__(self, letter):
        self.letter = letter
        self.index = -1
        self.outgoings = set()
        self.ingoings = set()

    def addOutgoing(self, outNode):
        self.outgoings.add(outNode)

    def addIngoing(self, inNode):
        self.ingoings.add(inNode)

    def setIndex(self, index):
        self.index = index

def checkCycles(nodes):
    processed = [0 for _ in range(index)]
    for node in nodes:
        if processed[node.index] == 0 and hasCycles(node, processed):
            return True
    return False

def hasCycles(node, processed):
    processed[node.index] = -1

    for out in node.outgoings:
        result = False
        if processed[out.index] == -1:
            result = True
        elif processed[out.index] == 0:
            result = hasCycles(out, processed)

        if result:
            return True

    processed[node.index] = 1

    return False

def getBuildSeq(node, processed):
    resSeq = ""
    for outgoing in node.outgoings:
        if (processed[outgoing.index] == 0):
            resSeq += getBuildSeq(outgoing, processed)
            processed[outgoing.index] = 1

    return resSeq + node.letter

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        r, c = map(int, input().split())

        wall = [input() for _ in range(r)]

        nodesDict = {}

        for i in range(r):
            for j in range(c):
                if not (wall[i][j] in nodesDict):
                    nodesDict[wall[i][j]] = Node(wall[i][j])

        for i in range(r - 1):
            for j in range(c):
                if wall[i + 1][j] != wall[i][j]:
                    nodesDict[wall[i][j]].addOutgoing(nodesDict[wall[i + 1][j]])
                    nodesDict[wall[i + 1][j]].addIngoing(nodesDict[wall[i][j]])

        nodesList = []
        index = 0

        for letter, node in nodesDict.items():
            node.setIndex(index)
            index += 1
            nodesList.append(node)

        if checkCycles(nodesList):
            print("Case #{}: -1".format(t))
        else:
            roots = filter(lambda node: len(node.ingoings) == 0, nodesList)
            processed = [0 for _ in range(index)]
            resSeq = []
            for root in roots:
                resSeq.append(getBuildSeq(root, processed))
            print("Case #{}: {}".format(t, "".join(resSeq)))


