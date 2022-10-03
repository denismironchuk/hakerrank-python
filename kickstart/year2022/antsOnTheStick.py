if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n, l = map(int, input().split())
        ants = []
        for i in range(n):
            position, direction = map(int, input().split())
            ants.append((i + 1, position, direction))

        ants = sorted(ants, key=lambda a: a[1])

        timeToFall = []

        leftSideToRightDirection, rightSideToLeftDirection = 0, 0
        leftSideIndex, rightSideIndex = -1, -1

        toLeftAnts = []
        toRightAnts = []

        for i in range(n):
            _, _, dir = ants[i]
            if dir == 0:
                toLeftAnts.append(ants[i])
                rightSideToLeftDirection += 1
                if (rightSideIndex == -1):
                    rightSideIndex = i
            else:
                toRightAnts.append(ants[i])

        toLeftIndex = -1
        toRightIndex = -1

        for i in range(n):
            index, pos, dir = ants[i]

            if dir == 0:
                # to left
                # <<<<<
                rightSideToLeftDirection -= 1
                toLeftIndex += 1
            else:
                toRightIndex += 1

            if dir == 0:
                # go left <<<
                if leftSideToRightDirection <= rightSideToLeftDirection:
                    timeToFall.append((index, toLeftAnts[toLeftIndex + leftSideToRightDirection][1]))
                else:
                    timeToFall.append((index, l - toRightAnts[toRightIndex - rightSideToLeftDirection][1]))
            else:
                #go right
                if leftSideToRightDirection >= rightSideToLeftDirection:
                    timeToFall.append((index, l - toRightAnts[toRightIndex - rightSideToLeftDirection][1]))
                else:
                    timeToFall.append((index, toLeftAnts[toLeftIndex + leftSideToRightDirection + 1][1]))

            if dir == 1:
                leftSideToRightDirection+=1

        timeToFall = sorted(timeToFall, key=lambda a: a[0])
        timeToFall = sorted(timeToFall, key=lambda a: a[1])
        res=" ".join(list(map(lambda a: str(a[0]), timeToFall)))
        print("Case #{}: {}".format(t, res))