MOD = 10 ** 9 + 7

def fastPow(n, pow):
    if pow == 0:
        return 1

    if pow % 2 == 0:
        return fastPow((n * n) % MOD, pow / 2)
    else:
        return (n * fastPow(n, pow - 1)) % MOD

print(((2 * 36 * 4 * fastPow(9 * 8 * 7, MOD - 2)) % MOD))