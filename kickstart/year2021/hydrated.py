def countDists(points, k):
    dist = 0
    firstCord = points[0][0]

    for cord, isFirst in points:
        if isFirst:
            dist += cord - firstCord

    prevCord = firstCord

    cntBefore = 0
    cntIn = 0
    cntAfter = k

    dists = []

    for cord, isFirst in points:
        dist = dist + cntBefore * (cord - prevCord) - cntAfter * (cord - prevCord)
        dists.append(dist)
        prevCord = cord
        if isFirst:
            cntAfter -= 1
            cntIn += 1
        else:
            cntBefore += 1
            cntIn -= 1

    return dists

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        k = int(input())
        points = [(x1, y1, x2, y2) for x1, y1, x2, y2 in [map(int, input().split()) for _ in range(k)]]
        verticalLines = []
        horizontalLines = []
        for x1, y1, x2, y2 in points:
            verticalLines.append((x1, True))
            verticalLines.append((x2, False))
            horizontalLines.append((y1, True))
            horizontalLines.append((y2, False))

        verticalLines.sort(key=lambda x: x[0])
        horizontalLines.sort(key=lambda y: y[0])

        vertDists = countDists(verticalLines, k)
        horDists = countDists(horizontalLines, k)

        minXDist = 99999999999999
        minX = -1

        for i, dist in enumerate(vertDists):
            if dist < minXDist:
                minXDist = dist
                minX = verticalLines[i][0]

        minYDist = 99999999999999
        minY = -1

        for i, dist in enumerate(horDists):
            if dist < minYDist:
                minYDist = dist
                minY = horizontalLines[i][0]

        print("Case #{}: {} {}".format(t, minX, minY))