def buildBinomials():
    binomials = {}
    for i in range(0, 51):
        binomials[i] = {0: 1, i: 1}

    for i in range(1, 51):
        for j in range(1, i):
            binomials[i][j] = binomials[i - 1][j - 1] + binomials[i - 1][j]

    return binomials

if __name__ == '__main__':
    t = int(input())

    bins = buildBinomials()

    for _ in range(t):
        n = int(input())
        y = list(map(int, input().split()))
        l = {}

        for k in y:
            lessElmnt = 0
            for e in y:
                if e < k:
                    lessElmnt += 1
            l[k] = lessElmnt

        expectVal = 0.0

        for k in y:
            for i in range(l[k] + 1):
                expectVal += bins[l[k]][i] / bins[n][i]

        print("{:.2f}".format(expectVal))