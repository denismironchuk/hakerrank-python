from math import sqrt, ceil, floor

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        d = n ** 2 - 4 * n * k
        if d > 0:
            i1 = floor((n - sqrt(d)) / 2)
            i2 = ceil((n + sqrt(d)) / 2)
            if (i1 < 1) | (i2 > n - 1):
                print(0)
            else:
                print(i1 + n - i2)
        else:
            print(n - 1)