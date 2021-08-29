if __name__ == '__main__':
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    horizontal = True
    vertical = True

    currentX, currentY = points[0]

    for x, y in points:
        if currentX != x:
            horizontal = False
        if currentY != y:
            vertical = False

        currentX = x
        currentY = y

    if horizontal | vertical:
        print("YES")
    else:
        print("NO")