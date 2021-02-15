if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        n = int(input())
        a = list(map(int, input().split()))
        diffs = []
        maxCnt = 0
        cnt = 0
        for i in range(1, n):
            newDiff = a[i] - a[i - 1]
            if (len(diffs) > 0 and newDiff == diffs[-1]):
                cnt += 1
            else:
                cnt = 1

            if (cnt > maxCnt):
                maxCnt = cnt

            diffs.append(newDiff)

        print("Case #{}: {}".format(t, maxCnt + 1))