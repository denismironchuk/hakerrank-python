def countMaxSumsToLeft(lst):
    res = [lst[0]]
    for v in lst[1:]:
        res += [v + max(0, res[-1])]

    return res

def countMaxSumsToRight(lst):
    return countMaxSumsToLeft(lst[::-1])[::-1]

def countMaxResToLeft(row, maxSum, maxSumsToLeft):
    maxResToLeft = [row[0] + maxSum[0]]

    for i in range(1, len(row)):
        maxResToLeft += [max(maxResToLeft[-1] + row[i], maxSumsToLeft[i] + maxSum[i])]

    return maxResToLeft


def countMaxResToRight(row, maxSum, maxSumsToRight):
    return countMaxResToLeft(row[::-1], maxSum[::-1], maxSumsToRight[::-1])[::-1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)][::-1]

    maxSum = [max(left, right, left + right - curr) for left, right, curr in zip(countMaxSumsToRight(matrix[0]), countMaxSumsToLeft(matrix[0]), matrix[0])]

    for row in matrix[1:]:
        maxSumsToRight = countMaxSumsToRight(row)
        maxSumsToLeft = countMaxSumsToLeft(row)

        maxResToRight = countMaxResToRight(row, maxSum, maxSumsToRight)
        maxResToLeft = countMaxResToLeft(row, maxSum, maxSumsToLeft)

        maxSum = [max(maxResToLeft[i], maxResToRight[i],
                      maxResToRight[i] + maxSumsToLeft[i] - row[i],
                      maxResToLeft[i] + maxSumsToRight[i] - row[i]) for i in range(len(row))]

    print(max(maxSum))

