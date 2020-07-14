from random import randrange

def countMaxSumsToRight(lst):
    return countMaxSumsToLeft(lst[::-1])[::-1]

def countMaxSumsToLeft(lst):
    res = [lst[0]]
    for v in lst[1:]:
        res += [v + max(0, res[-1])]

    return res

def countMaxResToLeft(row, maxSum):
    maxResToLeft = [row[0] + maxSum[0]]

    for i in range(1, len(row)):
        maxResToLeft += [row[i] + max(maxSum[i], maxResToLeft[-1])]

    return maxResToLeft


def countMaxResToRight(row, maxSum):
    return countMaxResToLeft(row[::-1], maxSum[::-1])[::-1]

if __name__ == '__main__':
    lst = [randrange(-100, 100) for i in range(20)]

    maxSum = [max(left, right, left + right - curr) for left, right, curr in
              zip(countMaxSumsToRight(lst), countMaxSumsToLeft(lst), lst)]

    print(lst)
    print(maxSum)

    # n, m = map(int, input().split())
    # matrix = [list(map(int, input().split())) for _ in range(n)][::-1]
    #
    # maxSum = [max(left, right, left + right - curr) for left, right, curr in zip(countMaxSumsToRight(matrix[0]), countMaxSumsToLeft(matrix[0]), matrix[0])]
    #
    # for row in matrix[1:]:
    #     maxSumsToRight = countMaxSumsToRight(row)
    #     maxSumsToLeft = countMaxSumsToLeft(row)
    #
    #     maxResToRight = countMaxResToRight(row, maxSum)
    #     maxResToLeft = countMaxResToLeft(row, maxSum)
    #
    #     maxSum = [max(maxResToLeft[i], maxResToRight[i],
    #                   maxResToRight[i] + maxSumsToLeft[i] - row[i],
    #                   maxResToLeft[i] + maxSumsToRight[i] - row[i]) for i in range(len(row))]
    #
    # print(max(maxSum))

