if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n = int(input())
        a = list(map(int, input().split()))
        exp = 0.0

        for positions in range(n - 1, 0, -1):
            exp += (sum(a) * 2 - a[0] - a[-1]) / positions
            newA = []
            for pos in range(positions):
                newVal = ((a[pos] + a[pos + 1]) + a[pos] * (positions - pos - 1) + a[pos + 1] * (pos)) / positions
                newA.append(newVal)
            a = newA

        print("Case #{}: {}".format(t, exp))