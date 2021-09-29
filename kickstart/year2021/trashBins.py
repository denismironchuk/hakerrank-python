if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n = int(input())
        s = input()

        bins = [int(c) for c in s]

        distsToLeft = [0 for _ in range(n)]
        distsToRight = [0 for _ in range(n)]

        distsToLeft[0] = 0 if bins[0] == 1 else 9999999999
        distsToRight[-1] = 0 if bins[-1] == 1 else 9999999999

        for i in range(1, n):
            if bins[i] == 1:
                distsToLeft[i] = 0
            else:
                distsToLeft[i] = distsToLeft[i - 1] + 1

            if bins[- i - 1] == 1:
                distsToRight[- i - 1] = 0
            else:
                distsToRight[- i - 1] = distsToRight[- i] + 1

        res = 0

        for i in range(n):
            res += min(distsToLeft[i], distsToRight[i])

        print("Case #{}: {}".format(t, res))


