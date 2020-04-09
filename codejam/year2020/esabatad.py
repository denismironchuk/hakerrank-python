from random import random, randrange

state = []
query = 1

def findEqualPos(b):
    l = len(b)
    for i in range(1, 1 + ((l - 1) // 2)):
        if (b[i] == -1 or b[l - i] == -1):
            return -1
        if (b[i] == b[l - i]):
            return i
    return -1

def findDifferentPos(b):
    l = len(b)
    for i in range(1, 1 + ((l - 1) // 2)):
        if (b[i] == -1 or b[l - i] == -1):
            return -1
        if ((b[i] == 1 and b[l - i] == 0) or (b[i] == 0 and b[l - i] == 1)):
            return i
    return -1

def determAndPerformEffect(b, itr):
    eqPos = findEqualPos(b)
    difPos = findDifferentPos(b)

    if (eqPos != -1 and difPos != -1):
        newEq = requestValue(eqPos)
        itr += 1
        newDif = requestValue(difPos)
        itr += 1

        if (b[eqPos] != newEq):
            if (b[difPos] != newDif):
                invert(b)
            else:
                flipInvert(b)
        else:
            if (b[difPos] != newDif):
                flip(b)
            else:
                doNothing(b)
    elif (eqPos != -1 and difPos == -1):
        clearUnpairedPos(b)
        newEq = requestValue(eqPos)
        itr += 1

        if (b[eqPos] != newEq):
            invert(b)
        else:
            doNothing(b)
    elif (eqPos == -1 and difPos != -1):
        clearUnpairedPos(b)
        newDif = requestValue(difPos)
        itr += 1

        if (b[difPos] != newDif):
            invert(b)
        else:
            doNothing(b)

    return itr

def clearUnpairedPos(b):
    l = len(b)
    for i in range(1, l):
        if (b[i] != -1 and b[l - i] == -1):
            b[i] = -1


def invert(b):
    for i in range(1,len(b)):
        if (b[i] != -1):
            b[i] = int(not b[i])
    return b

def flip(b):
    l = len(b)
    for i in range(1, 1 + ((l - 1) // 2)):
        b[i], b[l - i] = b[l - i], b[i]

    return b

def flipInvert(b):
    flip(b)
    invert(b)
    return b

def doNothing(b):
    return b

def hasUndefValues(b):
    for i in range(1, len(b)):
        if (b[i] == -1):
            return True

    return False

def generateState(length):
    return [-1] + [int(random() < 0.9) for _ in range(length)]

#def requestValue(pos):
#    print(pos)
#    return int(input())

def requestValue(pos):
    global query

    if ((query % 10) == 1):
        act = randrange(4)
        if (act == 0):
            invert(state)
        elif (act == 1):
            flip(state)
        elif (act == 2):
            flipInvert(state)

    query += 1
    return state[pos]

if __name__ == '__main__':
    T, B = map(int, input().split())

    for t in range(1, T + 1):
        query = 1
        state = generateState(B)
        b = [-1] * (B + 1)
        b[1] = requestValue(1)

        defPos = 1
        itr = 2

        while (hasUndefValues(b)):
            if (itr % 10 == 1):
                itr = determAndPerformEffect(b, itr)

            if (b[defPos] == -1):
                b[defPos] = requestValue(defPos)
                itr += 1
            elif (b[B + 1 - defPos] == -1):
                b[B + 1 - defPos] = requestValue(B + 1 - defPos)
                itr += 1
            else:
                defPos += 1

        print(''.join(map(str, b[1:])))
        response = input()
        if (response == 'N'):
            break
