if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        n = int(input())
        cords = []
        for _ in range(n):
            x, y = map(int, input().split())
            cords.append((x, y))

        xCords = list(map(lambda cord: cord[0], cords))
        yCords = list(map(lambda cord: cord[1], cords))

        xCords.sort()
        yCords.sort()

        res = 0

        for i in range(n // 2):
            res += yCords[-(i + 1)] - yCords[i]

        intervals = []
        for i in range(n - 1):
            intervals.append(xCords[i + 1] - xCords[i])

        singlePointMoves = [0]
        for i in range(n - 1):
            singlePointMoves[0] += (n - i - 1) * intervals[i]

        for i in range(n - 1):
            singlePointMoves.append(singlePointMoves[i] - (n - i - 1) * intervals[i] + intervals[i] * (i + 1))

        progression = [0]

        for i in range(1, n + 1):
            progression.append(progression[i - 1] + i)

        samePointsToLeft = [0]
        for i in range(1, len(xCords)):
            if (xCords[i] == xCords[i - 1]):
                samePointsToLeft.append(samePointsToLeft[i - 1] + 1)
            else:
                samePointsToLeft.append(0)

        samePointsToRight = [0 for _ in range(len(xCords))]
        for i in range(len(xCords) - 2, -1, -1):
            if (xCords[i] == xCords[i + 1]):
                samePointsToRight[i] = samePointsToRight[i + 1] + 1
            else:
                samePointsToRight[i] = 0

        for i in range(n - 1):
            singlePointMoves[i] -= progression[n - 1 - i]
            singlePointMoves[i] -= progression[i]

        print("Case #{}: {}".format(t, res + min(singlePointMoves)))
