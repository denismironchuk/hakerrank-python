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

    nodes = [None] + [Node(i) for i in range(1, n + 1)]

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
            for node in islandsMap[i]:
                node.inverseColor()

        val = 2 * abs(black - white)
        if (val not in valsIslandsMap):
            valsIslandsMap[val] = []
        valsIslandsMap[val].append(i)

        if (val not in valsCnt):
            valsCnt[val] = 0
        valsCnt[val] += 1

        vals.append(val)

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

    islandsToInvert = []

    while (sum != 0):
        if (cntTable[row_][sum] == 0):
            row_ -= 1
        else:
            islandsToInvert.append(valsIslandsMap[valsOrder[row_]][-1])
            valsIslandsMap[valsOrder[row_]].pop()
            sum -= valsOrder[row_]

    print(disp, island - 1)

    for islnd in islandsToInvert:
        for node in islandsMap[islnd]:
            node.inverseColor()

    islandColorMap = {}
    for i in range(island):
        islandColorMap[i] = {0: [], 1: []}
        for node in islandsMap[i]:
            islandColorMap[i][node.color].append(node)

    biColourIsland = -1

    for islnd, islndNodes in islandsMap.items():
        blackCount, whiteCount = 0, 0

        for node in islndNodes:
            if (node.color == 0):
                blackCount += 1
            else:
                whiteCount += 1

        if (blackCount != 0 and whiteCount != 0):
            biColourIsland = islnd
            break

    if biColourIsland != -1:
        # 0 - black
        # 1 - white
        biColourIslandBlackNodeNum = islandColorMap[biColourIsland][0][0].num
        biColourIslandWhiteNodeNum = islandColorMap[biColourIsland][1][0].num

        for islnd in range(island):
            if islnd == biColourIsland:
                continue

            if islandColorMap[islnd][0]:
                print(biColourIslandWhiteNodeNum, islandColorMap[islnd][0][0].num)
            else:
                print(biColourIslandBlackNodeNum, islandColorMap[islnd][1][0].num)
    else:
        #0 - white
        #1 - black
        whiteColourIsland = -1
        blackColorIsland = -1

        for islnd, islndNodes in islandsMap.items():
            if (whiteColourIsland != -1 and blackColorIsland != -1):
                break

            if (whiteColourIsland == -1 and islndNodes[0].color == 0):
                whiteColourIsland = islnd

            if (blackColorIsland == -1 and islndNodes[0].color == 1):
                blackColorIsland = islnd

        if (whiteColourIsland != -1 and blackColorIsland != -1):
            whiteNodeNum = islandsMap[whiteColourIsland][0].num
            blackNodeNum = islandsMap[blackColorIsland][0].num

            for islnd, islndNodes in islandsMap.items():
                if (islnd == whiteColourIsland or islnd == blackColorIsland):
                    continue

                if (islndNodes[0].color == 0):
                    print(blackNodeNum, islndNodes[0].num)
                else:
                    print(whiteNodeNum, islndNodes[0].num)

            print(whiteNodeNum, blackNodeNum)
