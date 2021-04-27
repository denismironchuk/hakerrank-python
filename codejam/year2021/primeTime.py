from math import log, ceil

def factorize(n, primes):
    res = []

    for p, primesCount in primes:
        if (n % p == 0):
            cnt = 0
            while (n % p == 0):
                n //= p
                cnt += 1

            if cnt > primesCount:
                return []

            res.append((p, cnt))

    if n == 1:
        return res
    else:
        return []

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        m = int(input())
        primes = []
        maxSum = 0
        for _ in range(m):
            p, n = map(int, input().split())
            primes.append((p, n))
            maxSum += p * n

        maxLim = 0
        for p, n in primes:
            maxLim += p * ceil(log(maxSum)/log(p))

        hasSolution = False
        for s in range(2, maxLim + 1):
            if maxSum - s < 2:
                break

            fact = factorize(maxSum - s, primes)
            if len(fact) > 0:
                primesSum = 0
                for p, cnt in fact:
                    primesSum += p * cnt

                if primesSum == s:
                    print("Case #{}: {}".format(t, maxSum - s))
                    hasSolution = True
                    break

        if not hasSolution:
            print("Case #{}: {}".format(t, 0))