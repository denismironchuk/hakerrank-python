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

        for i in range(n):
            _, _, dir = ants[i]
            if dir == 0:
                rightSideToLeftDirection += 1

        for i in range(n):
            index, pos, dir = ants[i]

            if dir == 0:
                # to left
                # <<<<<
                rightSideToLeftDirection -= 1

            if dir == 0:
                # go left <<<
                if leftSideToRightDirection <= rightSideToLeftDirection:
                    # falls from left end
                    # |------------
                    if leftSideToRightDirection == 0:
                        timeToFall.append((index, pos))
                    else:
                        expectedPosition = 0
                        k = i + 1
                        while expectedPosition != leftSideToRightDirection:
                            if (ants[k][2] == 0):
                                expectedPosition += 1

                            if (expectedPosition == leftSideToRightDirection):
                                break

                            k += 1

                        timeToFall.append((index, ants[k][1]))
                else:
                    # falls from right end
                    # -----------|
                    expectedPosition = 0
                    k = i
                    while expectedPosition != rightSideToLeftDirection + 1:
                        if (ants[k][2] == 1):
                            expectedPosition += 1

                        if (expectedPosition == rightSideToLeftDirection + 1):
                            break

                        k -= 1

                    timeToFall.append((index, l - ants[k][1]))

            else:
                #go right
                if leftSideToRightDirection >= rightSideToLeftDirection:
                    # falls from right end
                    # -------------|
                    if rightSideToLeftDirection == 0:
                        timeToFall.append((index, l - pos))
                    else:
                        expectedPosition = 0
                        k = i - 1
                        while expectedPosition != rightSideToLeftDirection:
                            if (ants[k][2] == 1):
                                expectedPosition += 1

                            if (expectedPosition == rightSideToLeftDirection):
                                break

                            k -= 1

                        timeToFall.append((index, l - ants[k][1]))
                else:
                    #falls from left end
                    expectedPosition = 0
                    k = i
                    while expectedPosition != leftSideToRightDirection + 1:
                        if (ants[k][2] == 0):
                            expectedPosition += 1

                        if (expectedPosition == leftSideToRightDirection + 1):
                            break

                        k += 1

                    timeToFall.append((index, ants[k][1]))

            if dir == 1:
                leftSideToRightDirection+=1

        timeToFall = sorted(timeToFall, key=lambda a: a[0])
        timeToFall = sorted(timeToFall, key=lambda a: a[1])
        res=" ".join(list(map(lambda a: str(a[0]), timeToFall)))
        print("Case #{}: {}".format(t, res))