if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        k = int(input())
        a = list(map(int, input().split()))
        aUnique = [a[0]]

        for i in range(1, k):
            if a[i] != a[i - 1]:
                aUnique.append(a[i])

        k = len(aUnique)
        if (k <= 4):
            print("Case #{}: {}".format(t, 0))
        else:
            direction = 1 if aUnique[1] > aUnique[0] else -1
            cnt = 2
            err = 0
            for i in range(2,  k):
                nextDirection = 1 if aUnique[i] > aUnique[i - 1] else -1
                if (direction == nextDirection):
                    cnt += 1
                else:
                    cnt = 2

                if (cnt == 5):
                    err += 1
                    cnt = 1

                direction = nextDirection

            print("Case #{}: {}".format(t, err))
