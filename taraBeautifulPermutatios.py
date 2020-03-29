from collections import Counter

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
        a = map(int, input().split())
        count = Counter(a)
        elmntLen = len(count.keys())

        res = [0, fact(elmntLen), 0, 0]

        for val, cnt in count.items():
            if (cnt == 1):
                continue

            newRes = [0]
            for i in range(1, len(res) - 1):
                newRes += [(res[i + 1] * i) % MOD]
                newRes[i] += (res[i] * (elmntLen - i)) % MOD
                newRes[i] %= MOD

                newRes[i] *= TWO
                newRes[i] %= MOD

                newRes[i] += res[i - 1]
                newRes[i] %= MOD

            elmntLen += 1
            newRes += [0, 0]
            res = newRes

        print(res[1])