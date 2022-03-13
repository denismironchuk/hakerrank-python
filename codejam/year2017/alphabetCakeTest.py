import random as rnd

def printCake(cake):
    for row in cake:
        print("".join(row))

if __name__ == '__main__':
    T = 100000

    for t in range(1, T + 1):
        r, c = 25, 25

        cells = []

        for r1 in range(r):
            for c1 in range(c):
                cells.append((r1, c1))

        cake = [['?' for _ in range(c)] for _ in range(r)]

        for letter in range(ord('A'), ord('Z') + 1):
            if (len(cells) == 0):
                break

            pos = rnd.randint(0, len(cells) - 1)
            cell = cells[pos]
            cake[cell[0]][cell[1]] = chr(letter)
            del cells[pos]

        cakeOriginal = [[cake[rowOrig][colOrig] for colOrig in range(c)] for rowOrig in range(r)]

        positions = []

        for row2 in range(r):
            for col2 in range(c):
                if (cake[row2][col2] != '?'):
                    positions.append((row2, col2))

        for row, col in positions:
            letter = cake[row][col]
            upLeft = (row, col)
            downRight = (row, col)

            #move up
            canMove = True
            row_ = upLeft[0] - 1
            while (row_ >= 0 and canMove):
                col_ = upLeft[1]
                for col_ in range(upLeft[1], downRight[1] + 1):
                    canMove = canMove and cake[row_][col_] == '?'

                if (canMove):
                    upLeft = (row_, upLeft[1])

                row_ -= 1

            # move right
            canMove = True
            col_ = downRight[1] + 1
            while (col_ < c and canMove):
                row_ = upLeft[0]
                for row_ in range(upLeft[0], downRight[0] + 1):
                    canMove = canMove and cake[row_][col_] == '?'

                if (canMove):
                    downRight = (downRight[0], col_)

                col_ += 1

            # move down
            canMove = True
            row_ = downRight[0] + 1
            while (row_ < r and canMove):
                col_ = upLeft[1]
                for col_ in range(upLeft[1], downRight[1] + 1):
                    canMove = canMove and cake[row_][col_] == '?'

                if (canMove):
                    downRight = (row_, downRight[1])

                row_ += 1

            # move left
            canMove = True
            col_ = upLeft[1] - 1
            while (col_ >= 0 and canMove):
                row_ = upLeft[0]
                for row_ in range(upLeft[0], downRight[0] + 1):
                    canMove = canMove and cake[row_][col_] == '?'

                if (canMove):
                    upLeft = (upLeft[0], col_)

                col_ -= 1

            for row_1 in range(upLeft[0], downRight[0] + 1):
                for col_1 in range(upLeft[1], downRight[1] + 1):
                    cake[row_1][col_1] = letter

        for row3 in range(r):
            for col3 in range(c):
             if cake[row3][col3] == '?':
                 print("Original:")
                 printCake(cakeOriginal)
                 print("Result:")
                 printCake(cake)
                 raise RuntimeError("Smth went wrong")


