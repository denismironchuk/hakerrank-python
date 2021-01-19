from random import random

def randomDice(probs):
    sums = [0]
    for i in range(0, len(probs)):
        sums.append(sums[i] + probs[i])
    rndVal = random()
    for i in range(1, len(probs) + 1):
        if rndVal >= sums[i - 1] and rndVal < sums[i]:
            return i

def buildSeq(probs, len):
    seq = [randomDice(probs)]
    for i in range(len - 1):
        dice = randomDice(probs)
        while (dice == seq[i]):
            dice = randomDice(probs)
        seq.append(dice)
    return seq


def matrixMul(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])

    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if (cols1 != rows2):
        raise Exception("Not corresponding matrices")

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def countExpectation(diceSides, probs):
    estimateExp = 0
    for val in range(diceSides):
        estimateExp += (val + 1) * probs[val]
    return estimateExp

def countSqrExpectation(diceSides, stepProbs, transProbs, seqLen):
    sqrExp = 0

    for step1Index in range(seqLen):
        probs = stepProbs[step1Index]
        for val in range(diceSides):
            sqrExp += ((val + 1) ** 2) * probs[val]

        itrProbs = [[0 for _ in range(diceSides)] for _ in range(diceSides)]
        for i in range(diceSides):
            itrProbs[i][i] = probs[i]

        for _ in range(step1Index + 1, seqLen):
            itrProbs = matrixMul(itrProbs, transProbs)
            for i in range(diceSides):
                for j in range(diceSides):
                    sqrExp += (i + 1) * (j + 1) * 2 * itrProbs[i][j]

    return sqrExp

if __name__ == '__main__':
    diceSides = 6
    probs = [0.12, 0.12, 0.1, 0.02, 0.14, 0.5]
    seqLen = 10

    transitionProb = [[0 for _ in range(diceSides)] for _ in range(diceSides)]
    for x_cur in range(diceSides):
        for x_prev in range(diceSides):
            if x_cur == x_prev:
                continue
            transitionProb[x_prev][x_cur] = probs[x_cur] / (sum(probs) - probs[x_prev])

    stepProbs = [[] + probs]
    estimateExp = countExpectation(diceSides, stepProbs[-1])

    for _ in range(seqLen - 1):
        stepProbs.append(matrixMul([stepProbs[-1]], transitionProb)[0])
        estimateExp += countExpectation(diceSides, stepProbs[-1])
    print("Estimated expectation:", estimateExp)
    estSqrExp = countSqrExpectation(diceSides, stepProbs, transitionProb, seqLen)
    print("Estimated sqr expectation:", estSqrExp)
    print("Estimated variance:", estSqrExp - estimateExp ** 2)
    print("=================")

    expVal = 0
    sqrExpVal = 0
    expDisp = 0
    for n in range(1000000):
        seqSum = sum(buildSeq(probs, seqLen))
        expVal = (expVal * n + seqSum) / (n + 1)
        sqrExpVal = (sqrExpVal * n + seqSum ** 2) / (n + 1)
        expDisp = (expDisp * n + (seqSum - estimateExp) ** 2) / (n + 1)

    print("Experiment expectation:", expVal)
    print("Experiment square value expectation:", sqrExpVal)
    print("Experiment variance:", expDisp)
