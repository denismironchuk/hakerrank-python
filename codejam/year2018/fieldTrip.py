import math

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n = int(input())
        cords = []
        for _ in range(n):
            x, y = map(int, input().split())
            cords.append((x, y))
        xSorted = sorted(cords, key=lambda x: x[0])
        ySorted = sorted(cords, key=lambda x: x[1])
        xDist = math.ceil((xSorted[-1][0] - xSorted[0][0]) / 2)
        yDist = math.ceil((ySorted[-1][1] - ySorted[0][1]) / 2)
        print("Case #{}: {}".format(t, max(xDist, yDist)))