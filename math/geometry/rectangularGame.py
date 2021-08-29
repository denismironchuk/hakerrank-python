if __name__ == '__main__':
    n = int(input())
    xCords = []
    yCords = []
    for _ in range(n):
        x, y = map(int, input().split())
        xCords.append(x)
        yCords.append(y)

    xCords.sort()
    yCords.sort()

    print(xCords[0] * yCords[0])