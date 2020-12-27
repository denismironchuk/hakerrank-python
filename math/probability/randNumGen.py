def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a, b, c = map(int, input().split())

        if (a + b <= c):
            print("1/1")
        else:
            p = c ** 2
            if (c > b):
                p -= (c - b) ** 2
            if (c > a):
                p -= (c - a) ** 2
            all = 2 * a * b
            g = gcd(all, p)
            print("{}/{}".format(int(p / g), int(all / g)))