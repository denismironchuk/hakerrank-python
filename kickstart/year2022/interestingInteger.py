def splitToSums(n, maxVal, maxCnt):
    if (maxCnt == 1):
        return [[n]] if n <= maxVal else []

    sums = []
    for i in range(maxVal, 0, -1):
        if n - i > 0:
            subSums = splitToSums(n - i, i, maxCnt - 1)
            for subSum in subSums:
                subSum.append(i)
                sums.append(subSum)
        elif n - i == 0:
            sums.append([i])

    return sums


res = 0

for n in range(2, 100):
    n_ = n
    fact = []
    i = 2

    while i * i <= n:
        while n % i == 0:
            fact.append(i)
            n //= i
        i += 1

    if n != 1:
        fact.append(n)

    valid = True
    for f in fact:
        valid = valid and (f < 10)

    if valid:
        splitCnt = len(splitToSums(n_ - sum(fact), 9, 11 - len(fact)))
        print("{} - {}, {}, {}, {}".format(n_, fact, sum(fact), n_ - sum(fact), splitCnt))
        res += splitCnt

print(res)
splittedSums = splitToSums(86, 9, 10)
for s in splittedSums:
    print(s[::-1])
