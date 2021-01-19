def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))

    isSorted = True
    for i in range(n - 1):
        if p[i] > p[i + 1]:
            isSorted = False

    if isSorted:
        print(0)
    else:
        cntMap = {}
        for val in p:
            if val not in cntMap:
                cntMap[val] = 0
            cntMap[val] += 1
        res = fact(n)

        for cnt in cntMap.values():
            res /= fact(cnt)

        print(res)