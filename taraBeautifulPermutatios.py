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

        res = [fact(elmntLen), 0, 0]

        for val, cnt in count.items():
            if (cnt == 1):
                continue

            prev = 0
            for i in range(0, len(res) - 1):
                newVal = (((res[i + 1] * (i + 1))) + ((res[i] * (elmntLen - i - 1)))) % MOD

                newVal *= TWO
                newVal %= MOD

                newVal += prev
                newVal %= MOD

                prev = res[i]

                res[i] = newVal

            elmntLen += 1
            res.append(0)

        print(res[0])