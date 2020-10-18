if __name__ == '__main__':
    T = int(input())

    MOD = 10 ** 9

    for t in range(1, T + 1):
        prog = input()

        nCnt = 0
        sCnt = 0
        eCnt = 0
        wCnt = 0
        mul = 1
        muls = [1]

        for c in prog:
            if c == 'N':
                nCnt += mul
                nCnt %= MOD

            if c == 'S':
                sCnt += mul
                sCnt %= MOD

            if c == 'E':
                eCnt += mul
                eCnt %= MOD

            if c == 'W':
                wCnt += mul
                wCnt %= MOD

            if c.isdigit():
                cnt = int(c)
                mul *= cnt
                mul %= MOD
                muls.append(mul)

            if c == ')':
                muls.pop()
                mul = muls[-1]

        x = 1 + (eCnt + (MOD - wCnt)) % MOD
        y = 1 + (sCnt + (MOD - nCnt)) % MOD

        print("Case #{}: {} {}".format(t, x, y))
