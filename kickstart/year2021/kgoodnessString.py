if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n, k = map(int, input().split())
        s = input()

        diff = 0

        for i in range(n):
            if (s[i] != s[-1 - i]):
                diff += 1

        diff //= 2

        print("Case #{}: {}".format(t, abs(diff - k)))
