from math import log2

logs = [-1] + [log2(i) for i in range(1, 200000)]
logFact = [0]

for i in range(1, 200000):
    logFact.append(logFact[-1] + logs[i])

def binLog(k, n):
    return logFact[n] - logFact[k] - logFact[n - k]

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        w, h, l, u, r, d = map(int, input().split())

        prob = 0.0

        startX = l - 1
        startY = d + 1

        n = startX + startY - 2

        if (startX > 0 and startY <= h):
            while (startX > 0 and startY < h):
                prob += 2 ** (binLog(startX - 1, n) - n)
                startX -= 1
                startY += 1

            if (startY == h):
                startY -= 1
                n -= 1
                while (startX > 0):
                    prob += 2 ** (binLog(startX - 1, n) - n - 1)
                    startX -= 1
                    n -= 1

        startX = r + 1
        startY = u - 1

        n = startX + startY - 2

        if (startX <= w and startY > 0):
            while (startX < w and startY > 0):
                prob += 2 ** (binLog(startX - 1, n) - n)
                startX += 1
                startY -= 1

            if (startX == w):
                startX -= 1
                n -= 1
                while (startY > 0):
                    prob += 2 ** (binLog(startY - 1, n) - n - 1)
                    startY -= 1
                    n -= 1

        print("Case #{}: {}".format(t, prob))