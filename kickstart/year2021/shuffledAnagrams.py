if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        s = input()
        counts = {}
        for c in s:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1

        cntTuples = []

        for c, cnt in counts.items():
            cntTuples.append((c, cnt))

        cntTuples.sort(key=lambda tp: tp[1], reverse=True)
        maxGroupSize = cntTuples[0][1]
        totalLen = len(s)
        if (maxGroupSize * 2 > totalLen):
            print("Case #{}: IMPOSSIBLE".format(t))
        else:
            sortedLetters = []
            for c, cnt in cntTuples:
                for _ in range(cnt):
                    sortedLetters.append(c)

            shiftedLetters = []
            substs = {}
            for i in range(totalLen):
                if sortedLetters[i] not in substs:
                    substs[sortedLetters[i]] = []
                substs[sortedLetters[i]].append(sortedLetters[(totalLen - maxGroupSize + i) % totalLen])
                shiftedLetters.append(sortedLetters[(totalLen - maxGroupSize + i) % totalLen])

            res = []

            for c in s:
                rep = substs[c].pop()
                res.append(rep)

            print("Case #{}: {}".format(t, "".join(res)))
