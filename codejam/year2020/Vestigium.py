if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n = int(input())
        m = [list(map(int, input().split())) for _ in range(n)]
        trace = 0
        cols = 0
        rows = 0
        for i in range(n):
            trace += m[i][i]
            rowUnique = len(set(m[i]))
            colUnique = len(set([m[j][i] for j in range(n)]))
            if (rowUnique != n):
                rows += 1
            if (colUnique != n):
                cols += 1
        print("Case #{}: {} {} {}".format(t, trace, rows, cols))
