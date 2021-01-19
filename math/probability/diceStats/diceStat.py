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

if __name__ == '__main__':
    diceSides = 6
    probs = [0.8, 0.1, 0.04, 0.02, 0.02, 0.02]
    seqLen = 100
    expVal = 0
    for n in range(100000):
        seqSum = sum(buildSeq(probs, seqLen))
        expVal = (expVal * n + seqSum) / (n + 1)

    print(expVal)

    condProbs = [[0 for _ in range(diceSides)] for _ in range(diceSides)]
    for x_cur in range(diceSides):
        for x_prev in range(diceSides):
            if x_cur == x_prev:
                continue
            condProbs[x_cur][x_prev] = probs[x_cur] / (sum(probs) - probs[x_prev])

    absProbs = [probs]
    for i in range(seqLen - 1):
        newProbs = []
        for cur_dice in range(diceSides):
            newProb = 0
            for prev_dice in range(diceSides):
                newProb += condProbs[cur_dice][prev_dice] * absProbs[i][prev_dice]
            newProbs.append(newProb)
        absProbs.append(newProbs)

    estimateExp = 0

    for p in absProbs:
        for val in range(diceSides):
            estimateExp += (val + 1) * p[val]

    print("Estimated expectation:", estimateExp)

