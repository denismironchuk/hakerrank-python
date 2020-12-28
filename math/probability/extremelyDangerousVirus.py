MOD = 10 ** 9 + 7

class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __mul__(self, other):
        if self.cols != other.rows:
            raise RuntimeError

        resMatrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                for k in range(self.cols):
                    resMatrix[row][col] += (self.matrix[row][k] * other.matrix[k][col]) % MOD
                    resMatrix[row][col] %= MOD

        return Matrix(resMatrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def buildUnityMatrix(side):
        return Matrix([[1 if col == row else 0 for col in range(side)] for row in range(side)])

def fastPow(a, pow):
    if (pow == 0):
        return 1

    if (pow % 2 == 0):
        return fastPow((a * a) % MOD, pow // 2)
    else:
        return (a * fastPow(a, pow - 1)) % MOD

def fastPowMatrix(m, pow):
    if (pow == 0):
        return Matrix.buildUnityMatrix(m.rows)

    if (pow % 2 == 0):
        return fastPowMatrix(m * m, pow // 2)
    else:
        return m * fastPowMatrix(m, pow - 1)

if __name__ == '__main__':
    a, b, t = map(int, input().split())
    matrix = Matrix([[a, a], [b, b]])
    resMatr = fastPowMatrix(matrix, t)
    res = (((resMatr[0][0] + resMatr[1][0]) % MOD) * fastPow(fastPow(2, MOD - 2), t)) % MOD
    print(res)