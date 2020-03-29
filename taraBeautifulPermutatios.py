MOD = 10 ** 9 + 7
TWO = (MOD + 1) // 2

def fact(n):
    res = 1
    for i in range(1,n+1):
        res = (res * i) % MOD

    return res

def calc(prev, cur, next, i, len):
    return (((((((next * (i + 1)) % MOD) + ((cur * (len - i - 1))) % MOD) % MOD) * TWO) % MOD) + prev) % MOD

if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        doubLen = len([a[i] for i in range(n - 1) if a[i] == a[i + 1]])
        elmntLen = n - doubLen

        res = [0, 0, fact(elmntLen), 0, 0]

        for i in range(doubLen):
            res = [0,0] + [calc(prev, cur, next, index, elmntLen) for prev, cur, next, index in zip(res, res[1:], res[2:], range(-1, i + 3))][1:] + [0,0]
            elmntLen += 1

        print(res[2])