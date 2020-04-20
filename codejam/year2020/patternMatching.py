def comparePatternWithFixedString(fixed, pattern):
    ptrnParts = pattern.split("*")
    if (fixed and not pattern.startswith("*")):
        if (fixed.find(ptrnParts[0]) != 0):
            return False
        fixed = fixed[len(ptrnParts[0]):]
        ptrnParts = ptrnParts[1:]

    if (fixed and not pattern.endswith("*")):
        if (not fixed.endswith(ptrnParts[-1])):
            return False

        fixed = fixed[:len(fixed) - len(ptrnParts[-1])]
        ptrnParts = ptrnParts[:-1]

    if (not ptrnParts):
        return True

    for ptrnPart in ptrnParts:
        pos = fixed.find(ptrnPart)
        if (pos == -1):
            return False
        fixed = fixed[pos + len(ptrnPart):]

    return True

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n = int(input())
        patterns = [input() for _ in range(n)]
        noStar = list(filter(lambda ptrn : ptrn.find("*") == -1, patterns))

        if (noStar):
            noStarPtrn = noStar[0]

            if (len(noStar) > 1):
                noMatch = False
                for ptrn in noStar:
                    if (ptrn != noStarPtrn):
                        print("Case #{}: *".format(t))
                        noMatch = True
                        break
                if (noMatch):
                    break

            noMatch = False
            for ptrn in patterns:
                if (not comparePatternWithFixedString(noStarPtrn, ptrn)):
                    print("Case #{}: *".format(t))
                    noMatch = True
                    break

            if (noMatch):
                continue

            print("Case #{}: {}".format(t, noStarPtrn))
            break

        patternBegin = ""
        noStarInBegin = [pattern.split("*")[0] for pattern in patterns if not pattern.startswith("*")]
        if (noStarInBegin):
            noStarInBegin.sort(key=lambda str : len(str))
            lastPtrn = noStarInBegin[-1]
            noMatch = False
            for ptrn in noStarInBegin:
                if lastPtrn.find(ptrn) != 0:
                    print("Case #{}: *".format(t))
                    noMatch = True
                    break

            if (noMatch):
                continue

            patternBegin = lastPtrn

        patternEnd = ""
        noStarInTheEnd = [pattern.split("*")[-1] for pattern in patterns if not pattern.endswith("*")]
        if (noStarInTheEnd):
            noStarInTheEnd.sort(key=lambda str : len(str))
            lastPtrn = noStarInTheEnd[-1]
            noMatch = False
            for ptrn in noStarInTheEnd:
                if (not lastPtrn.endswith(ptrn)):
                    print("Case #{}: *".format(t))
                    noMatch = True
                    break

            if (noMatch):
                continue

            patternEnd = lastPtrn

        ptrnsToProc = [pattern.split('*')[1:-1] for pattern in patterns]

        result = patternBegin

        for ptrnToProc in ptrnsToProc:
            result += "".join(ptrnToProc)

        result += patternEnd

        print("Case #{}: {}".format(t, result))