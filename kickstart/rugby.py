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
            res += abs(xCords[-(i + 1)] - xCords[i] - (n - (2 * i) - 1))

        print("Case #{}: {}".format(t, res))
