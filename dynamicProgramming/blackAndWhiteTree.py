from random import randrange

class Node():
    def __init__(self, num):
        self.num = num
        self.neighbours = []

    def addNeighbour(self, neigh):
        self.neighbours.append(neigh)

    def inverseColor(self):
        self.color = (self.color + 1) % 2

def markTree(nd, islandNum, color, processed):
    nd.islandNum = islandNum
    nd.color = color

    for neigh in nd.neighbours:
        if (not processed[neigh.num]):
            processed[neigh.num] = True
            markTree(neigh, islandNum, (color + 1) % 2, processed)

if __name__ == '__main__':
    n, m = map(int, input().split())

    nodes = [-1] + [Node(i) for i in range(1, n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        nodes[u].addNeighbour(nodes[v])
        nodes[v].addNeighbour(nodes[u])

    processed = [False for i in range(0, n + 1)]
    island = 0

    for num in range(1, n + 1):
        if (not processed[num]):
            markTree(nodes[num], island, 0, processed)
            island += 1

    islandsMap = {}

    for node in nodes:
        if node:
            if node.islandNum not in islandsMap:
                islandsMap[node.islandNum] = []

            islandsMap[node.islandNum].append(node)

    blackWhiteCnt = [[0, 0] for _ in range(island)]

    for node in nodes[1:]:
        blackWhiteCnt[node.islandNum][node.color] += 1

    valsIslandsMap = {}
    vals = []
    valsCnt = {}

    for i in range(island):
        black, white = blackWhiteCnt[i]
        if (black > white):
            blackWhiteCnt[i] = [white, black]
            for nodes in islandsMap[i]:
                node.inverseColor()

        val = 2 * abs(black - white)
        if (val not in valsIslandsMap):
            valsIslandsMap[val] = []
        valsIslandsMap[val].append(i)

        if (val not in valsCnt):
            valsCnt[val] = 0
        valsCnt[val] += 1

        vals.append(val)

    islandColorMap = {}

    for i in range(island):
        islandColorMap[i] = {0:[], 1:[]}
        for node in islandsMap[i]:
            islandColorMap[i][node.color].append(node)

    maxVal = sum(vals)

    dynTable = [[0 for column in range(maxVal + 1)] for row in range(len(valsCnt))]
    cntTable = [[0 for column in range(maxVal + 1)] for row in range(len(valsCnt))]

    row = 0

    valsOrder = []

    for val, cnt in valsCnt.items():
        valsOrder.append(val)
        dynTable[row][0] = 1

        if (row == 0):
            for col in range(maxVal + 1):
                if (col - val < 0):
                    continue

                if (cntTable[row][col - val] < cnt and dynTable[row][col - val] == 1):
                    dynTable[row][col] = 1
                    cntTable[row][col] = cntTable[row][col - val] + 1
        else:
            for col in range(maxVal + 1):
                if (col - val < 0):
                    dynTable[row][col] = dynTable[row - 1][col]
                    continue

                if (cntTable[row][col - val] < cnt and dynTable[row][col - val] > dynTable[row - 1][col]):
                    dynTable[row][col] = 1
                    cntTable[row][col] = cntTable[row][col - val] + 1
                else:
                    dynTable[row][col] = dynTable[row - 1][col]

        row += 1

    sum = maxVal // 2
    row_ = row - 1
    disp = 0

    while (dynTable[row_][sum - disp] == 0 and dynTable[row_][sum + disp] == 0):
        disp += 1

    sum += disp

    islandsToInvert = {}

    while (sum != 0):
        if (cntTable[row_][sum] == 0):
            row_ -= 1
        else:
            islandsToInvert.add(valsIslandsMap[valsOrder[row_]][-1])
            valsIslandsMap[valsOrder[row_]].pop()
            sum -= valsOrder[row_]

    #TODO maybe incorrect from this place. check it tommorrow
    print(disp, len(islandsToInvert))

    islands1 = []
    islands2 = []

    for i in range(island):
        if (i in islandsToInvert):
            islands1.append(i)
        else:
            islands2.append(i)



    pass
