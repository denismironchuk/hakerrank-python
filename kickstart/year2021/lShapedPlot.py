def countShapes(len1, len2):
    res = 0

    if (len1 > 1 and len2 > 1):
        maxLen = max(len1, len2)
        minLen = min(len1, len2)

        if (minLen * 2 <= maxLen):
            res += minLen - 1
        else:
            res += (maxLen // 2) - 1

        res += (minLen // 2) - 1

    return res

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        r, c = map(int, input().split())

        grid = []
        for row in range(r):
            grid.append(list(map(int, input().split())))

        toLeftCnt = [[0 for _ in range(c)] for _ in range(r)]
        toRightCnt = [[0 for _ in range(c)] for _ in range(r)]
        toUpCnt = [[0 for _ in range(c)] for _ in range(r)]
        toDownCnt = [[0 for _ in range(c)] for _ in range(r)]

        for row in range(r):
            if (grid[row][-1] == 1):
                toRightCnt[row][-1] = 1

            for col in range(c - 2, -1, -1):
                if (grid[row][col] == 1):
                    toRightCnt[row][col] = toRightCnt[row][col + 1] + 1

            if (grid[row][0]) == 1:
                toLeftCnt[row][0] = 1

            for col in range(1, c):
                if (grid[row][col] == 1):
                    toLeftCnt[row][col] = toLeftCnt[row][col - 1] + 1

        for col in range(c):
            if (grid[0][col] == 1):
                toUpCnt[0][col] = 1

            for row in range(1, r):
                if (grid[row][col] == 1):
                    toUpCnt[row][col] = toUpCnt[row - 1][col] + 1

            if (grid[-1][col] == 1):
                toDownCnt[-1][col] = 1

            for row in range(r - 2, -1, -1):
                if (grid[row][col] == 1):
                    toDownCnt[row][col] = toDownCnt[row + 1][col] + 1

        res = 0

        for row in range(r):
            for col in range(c):
                if (grid[row][col] == 0):
                    continue

                res += countShapes(toUpCnt[row][col], toLeftCnt[row][col])
                res += countShapes(toUpCnt[row][col], toRightCnt[row][col])
                res += countShapes(toDownCnt[row][col], toLeftCnt[row][col])
                res += countShapes(toDownCnt[row][col], toRightCnt[row][col])


        print("Case #{}: {}".format(t, res))