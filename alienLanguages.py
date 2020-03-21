from datetime import datetime

MOD = 100000007

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n,m = map(int, input().split())

        start = datetime.now()

        step = [0]
        for i in range(1, n + 1):
            step.append(int(2 * i > n))

        stepsCumSum = []

        haveNonZero = True
        while (haveNonZero):
            stepCumSum = [0 for _ in range(0, n + 1)]
            stepCumSum[-1] = step[-1]
            for i in range(n - 1, 0, -1):
                stepCumSum[i] = (stepCumSum[i + 1] + step[i]) % MOD

            stepsCumSum.append(stepCumSum)

            haveNonZero = False
            step = [0]
            for i in range(1, n + 1):
                if (2 * i > n):
                    step.append(0)
                else:
                    newVal = stepsCumSum[-1][i * 2]
                    step.append(newVal)
                    haveNonZero = haveNonZero or newVal > 0

        sums = [s[1] for s in stepsCumSum]

        res = [1]

        for i in range(m):
            newVal = 0
            for j in range(len(sums)):
                if (len(res) - j > 0):
                    newVal += (res[-1 - j] * sums[j]) % MOD
                    newVal %= MOD

            res.append(newVal)

        end = datetime.now()

        print((end - start).total_seconds())

        print(res[-1])
