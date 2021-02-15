if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        n = int(input())
        v = list(map(int, input().split()))
        res = 0

        if n == 1:
            res = 1
        else:
            maxVal = -1
            for i in range(0, n - 1):
                if (v[i] > maxVal):
                    maxVal = v[i]
                    if (v[i] > v[i + 1]):
                        res += 1

            if (v[n - 1] > maxVal):
                res += 1

        print("Case #{}: {}".format(t, res))
