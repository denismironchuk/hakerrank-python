def isRoaring(year):
    digitsCnt = len(year)
    for d in range(1, digitsCnt):
        start = int(year[:d])
        testYear = buildYearFromStart(start, year)
        if (testYear == year):
            return True

    return False

def buildYearFromStart(start, year):
    testYear = str(start)
    while (len(testYear) < len(year)):
        start += 1
        testYear += str(start)
    return testYear

    if (len(testYear) == len(year)):
        return True

def getNextRoaringYear(year):
    candidates = []
    while (len(candidates) == 0):
        digitsCnt = len(year)
        for d in range(digitsCnt - 1, 0, -1):
            start = int(year[:d])
            testYear = buildYearFromStart(start, year)
            if (len(testYear) == len(year) and int(year) < int(testYear)):
                candidates.append(testYear)

            start = int(year[:d]) + 1
            testYear = buildYearFromStart(start, year)
            if (len(testYear) == len(year) and int(year) < int(testYear)):
                candidates.append(testYear)

            for start in range(int('9' * d) - 15, int('9' * d) + 1):
                if (start <= 0):
                    continue

                testYear = buildYearFromStart(start, year)
                if (len(testYear) == len(year) and int(year) < int(testYear)):
                    candidates.append(testYear)

        year = str(10 ** digitsCnt)

    years = list(map(int, candidates))
    years = sorted(years)

    return years[0]



if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        year = input()
        print("Case #{}: {}".format(t, getNextRoaringYear(year)))