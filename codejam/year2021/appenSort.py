def compare(val1, val2):
    if int(val1) < int(val2):
        return val2

    if (len(val1) < len(val2)):
        return val2
    elif (len(val1) == len(val2)):
        val2IsGreater = False
        for i in range(len(val1)):
            d1 = int(val1[i])
            d2 = int(val2[i])
            if (d1 > d2):
                break

            if (d1 < d2):
                val2IsGreater = True
                break

        if (val2IsGreater):
            return val2
        else:
            return val2 + '0'
    else:
        val2IsGreater = False
        val1IsGreater = False
        for i in range(len(val2)):
            d1 = int(val1[i])
            d2 = int(val2[i])
            if (d1 > d2):
                val1IsGreater = True
                break

            if (d1 < d2):
                val2IsGreater = True
                break

        if (val1IsGreater):
            for _ in range(len(val1) - len(val2) + 1):
                val2 += '0'
            return val2

        if (val2IsGreater):
            for _ in range(len(val1) - len(val2)):
                val2 += '0'
            return val2

        newVal = val2
        for _ in range(len(val1) - len(val2)):
            newVal += '9'

        if (newVal == val1):
            for _ in range(len(val1) - len(val2) + 1):
                val2 += '0'
            return val2
        else:
            return str(int(val1) + 1)

if __name__ == '__main__':
    #v1 = '900'
    #v2 = '9'
    #print(v1)
    #r = compare(v1, v2)
    #print(r)

    T = int(input())

    for t in range(1, T + 1):
        n = int(input())
        xList = input().split()
        res = 0
        for i in range(len(xList) - 1):
            prevLen = len(xList[i + 1])
            newVal = compare(xList[i], xList[i + 1])
            res += len(newVal) - prevLen
            xList[i + 1] = newVal

        print("Case #{}: {}".format(t, res))

