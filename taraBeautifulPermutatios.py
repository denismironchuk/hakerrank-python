MOD = 10 ** 9 + 7
TWO = (MOD + 1) // 2

def fact(n):
    res = 1
    for i in range(1,n+1):
        res = (res * i) % MOD

    return res

if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        doubLen = len([a[i] for i in range(n - 1) if a[i] == a[i + 1]])
        elmntLen = n - doubLen

        res = [fact(elmntLen), 0, 0]

        for i in range(doubLen):
            prev = 0
            for i in range(0, i + 2):
                newVal = (((res[i + 1] * (i + 1)) % MOD) + ((res[i] * (elmntLen - i - 1))) % MOD) % MOD

                newVal *= TWO
                newVal %= MOD

                newVal += prev
                newVal %= MOD

                prev = res[i]

                res[i] = newVal

            elmntLen += 1
            res.append(0)

        print(res[0])