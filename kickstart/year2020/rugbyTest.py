from random import randrange

n = 5
xLim = (-5, 5)
yLim = (-5, 5)

def brutforce(distsAll, row, procColumns):
    if (row == len(distsAll)):
        return 0;

    dists = distsAll[row]
    res = 999999999
    for c in range(len(dists)):
        if (c in procColumns):
            continue
        procColumns.add(c)
        res = min(res, brutforce(distsAll, row + 1, procColumns) + dists[c])
        procColumns.remove(c)

    return res

def countTrivial(points):
    res = 99999999
    for x in range(xLim[0], xLim[1]):
        for y in range(yLim[0], yLim[1]):
            linePoints = []
            for i in range(n):
                linePoints.append((x + i, y))

            distsAll = []
            for point in points:
                distsOne = []
                for linePoint in linePoints:
                    distsOne.append(abs(point[0] - linePoint[0]) + abs(point[1] - linePoint[1]))
                distsAll.append(distsOne)

            res = min(res, brutforce(distsAll, 0, set([])))

    return res

if __name__ == '__main__':
    while (True):
        print("================")
        cords = []
        for _ in range(n):
            cords.append((randrange(xLim[0], xLim[1]), randrange(yLim[0], yLim[1])))

        xCords = list(map(lambda cord: cord[0], cords))
        yCords = list(map(lambda cord: cord[1], cords))

        xCords.sort()
        yCords.sort()

        if (xCords[n // 2] == xCords[n // 2 + 1] or xCords[n // 2] == xCords[n // 2  - 1]):
            continue

        resOptimal = 0

        for i in range(n // 2):
            resOptimal += yCords[-(i + 1)] - yCords[i]
            resOptimal += abs(xCords[-(i + 1)] - xCords[i] - (n - (2 * i) - 1))

        print(resOptimal)
        resTriv = countTrivial(cords)
        print(resTriv)

        if (resOptimal != resTriv):
            #print(cords)
            raise RuntimeError(cords)
