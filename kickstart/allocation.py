if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n, b = map(int, input().split())
        a = map(int, input().split())
        a = sorted(a)

        sum = 0
        cnt = 0

        for cost in a:
            if (sum + cost <= b):
                sum += cost
                cnt += 1
            else:
                break

        print("Case #{}: {}".format(t, cnt))