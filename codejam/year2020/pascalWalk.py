def getTrianglePath(startRow, startCol, direction):
    path = []
    if (direction == 1):
        nextRow = startCol - 1
        for row in range(startRow - 1, nextRow, -1):
            if (direction == 1):
                for col in range(startCol, row + 1):
                    path.append((row, col))
            else:
                for col in range(row, startCol - 1, -1):
                    path.append((row, col))

            direction *= -1
    else:
        nextRow = startRow - startCol
        for row in range(startRow - 1, nextRow, -1):
            if (direction == -1):
                for col in range(row - nextRow, 0, -1):
                    path.append((row, col))
            else:
                for col in range(1, row - nextRow + 1):
                    path.append((row, col))

            direction *= -1

    return path

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n = int(input())
        nonZeroPos = []
        pos = 1
        n_ = n
        while (n_ != 0):
            if (n_ % 2 == 1):
                nonZeroPos.append(pos)
            n_ //= 2
            pos += 1

        path = []

        indexPos = len(nonZeroPos) - 1
        direction = 1
        while (indexPos >= 0):
            row = nonZeroPos[indexPos]

            nextRow = 0
            if (indexPos != 0):
                nextRow = nonZeroPos[indexPos - 1]

            if (direction == 1):
                for i in range(1, nextRow + 2):
                    path.append((row, i))

                path += getTrianglePath(row, nextRow + 1, 1)
            else:
                for i in range(row, row - nextRow - 1, -1):
                    path.append((row, i))

                path += getTrianglePath(row, row - nextRow, -1)

            indexPos -= 1
            direction *= -1

        print("Case #{}:".format(t))
        for n,m in reversed(path):
            print(n, m)