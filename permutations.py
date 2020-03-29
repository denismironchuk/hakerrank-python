from itertools import permutations

def buildZeroPairs(perm, val):
    zero = []

    lst = list(perm)
    ind = lst.index(val)

    for j in range(ind):
        newZeroList = list(perm)
        newZeroList.insert(j,val)
        zero += [newZeroList]

    for j in range(ind + 2, len(lst) + 1):
        newZeroList = list(perm)
        newZeroList.insert(j,val)
        zero += [newZeroList]

    return zero

def buildOnePairs(perm, val):
    newOneList = list(perm)
    ind = newOneList.index(1)
    newOneList.insert(ind, val)

    return newOneList

def splitPair(perm, pairVal, newVal):
    newList = list(perm)
    ind = newList.index(pairVal)
    newList.insert(ind + 1, newVal)

    return newList

if __name__ == '__main__':
    n = 4
    perms = permutations(range(1, n + 1))

    zero = []
    one = []

    for perm in perms:
        one += [buildOnePairs(perm, 1)]
        zero += buildZeroPairs(perm, 1)

    zero.sort()
    zero = zero[::2]
    one.sort()

    print("Zero", len(zero))

    for p in zero:
        print(p)

    print("One", len(one))

    for p in one:
        print(p)

    newZero = []

    for perm in zero:
        newZero += buildZeroPairs(perm, 2)

    for perm in one:
        newZero += [splitPair(perm, 1, 2)]

    newZero.sort()

    print("Zero", len(newZero))

    for p in newZero:
        print(p)

    print(newZero[::2] == newZero[1::2])