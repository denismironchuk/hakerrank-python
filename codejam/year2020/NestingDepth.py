if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        s = map(int, list(input()))
        res = ''
        depth = 0
        for d in s:
            if (d > depth):
                res += '(' * (d - depth)
            elif (d < depth):
                res += ')' * (depth - d)
            res += str(d)
            depth = d
        res += ')' * depth

        print("Case #{}: {}".format(t, res))