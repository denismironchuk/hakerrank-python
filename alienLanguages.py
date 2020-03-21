from datetime import datetime

MOD = 100000007

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n,m = map(int, input().split())

        #d1 = datetime.now()

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
            for i in range(1, n + 1):
                if (2 * i > n):
                    step[i] = 0
                else:
                    newVal = stepsCumSum[-1][i * 2]
                    step[i] = newVal
                    haveNonZero = haveNonZero or newVal > 0

        #d2 = datetime.now()

        sums = [s[1] for s in stepsCumSum]
        res = [1] + [0 for _ in range(len(sums) - 1)]

        for _ in range(m):
            res = [sum([(a * b) % MOD for a, b in zip(sums, res)]) % MOD] + res[:-1]

        #d3 = datetime.now()

        #print((d2 - d1).total_seconds())
        #print((d3 - d2).total_seconds())

        print(res[0])
