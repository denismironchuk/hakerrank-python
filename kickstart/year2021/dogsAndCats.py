if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n, d, c, m = map(int, input().split())
        animals = input()
        dogsCnt = sum([1 for a in animals if a == 'D'])
        if dogsCnt == 0:
            print("Case #{}: YES".format(t))
        else:
            canFeed = True
            for a in animals:
                if dogsCnt == 0 or not canFeed:
                    break

                if a == 'C':
                    if c > 0:
                        c -= 1
                    else:
                        canFeed = False

                if a == 'D':
                    if d > 0:
                        d -= 1
                        c += m
                        dogsCnt -= 1
                    else:
                        canFeed = False

            if canFeed:
                print("Case #{}: YES".format(t))
            else:
                print("Case #{}: NO".format(t))