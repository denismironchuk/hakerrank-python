import sys
from datetime import datetime
from itertools import accumulate

MOD = 10 ** 9 + 7
TWO = (MOD + 1) // 2

def calc(prev, cur, next, i, len):
    dif = next - cur + MOD
    return (((dif * (i + 1) + cur * len) * TWO) + prev) % MOD

if __name__ == '__main__':
    with open('C:\\Users\\dmiro\\test.txt', 'r') as sys.stdin:
        q = int(input())

        d1 = datetime.now()

        f = list(accumulate(range(1, 2001), lambda a, b : ((a * b) % MOD)))

        for _ in range(q):
            n = int(input())
            a = list(map(int, input().split()))
            a.sort()
            doubLen = len([_ for cur, next in zip(a, a[1:]) if cur == next])
            #doubLen = len([a[i] for i in range(n - 1) if a[i] == a[i + 1]])
            elmntLen = n - doubLen
            res = [0, 0, f[elmntLen - 1], 0, 0]

            for i in range(doubLen):
                res = [0,0] + [calc(prev, cur, next, index, elmntLen) for prev, cur, next, index in zip(res, res[1:], res[2:], range(-1, i + 3))][1:] + [0,0]
                elmntLen += 1

            print(res[2])

        d2 = datetime.now()

        print((d2 - d1).total_seconds())