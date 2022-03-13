if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        r, c = map(int, input().split())
        cake = [list(input()) for _ in range(r)]
        positions = []

        for col in range(c):
            for row in range(r):
                if cake[row][col] == '?':
                    continue

                letter = cake[row][col]

                row2 = row - 1
                while row2 >= 0 and cake[row2][col] == '?':
                    cake[row2][col] = letter
                    row2 -= 1

        for col in range(c):
            for row in range(r):
                if cake[row][col] == '?':
                    continue

                letter = cake[row][col]

                row2 = row + 1
                while row2 < r and cake[row2][col] == '?':
                    cake[row2][col] = letter
                    row2 += 1

        for col in range(c):
            for row in range(r):
                if cake[row][col] == '?':
                    continue

                letter = cake[row][col]

                col2 = col + 1
                while col2 < c and cake[row][col2] == '?':
                    cake[row][col2] = letter
                    col2 += 1

        for col in range(c):
            for row in range(r):
                if cake[row][col] == '?':
                    continue

                letter = cake[row][col]

                col2 = col - 1
                while col2 >= 0 and cake[row][col2] == '?':
                    cake[row][col2] = letter
                    col2 -= 1

        print("Case #{}:".format(t))
        for row3 in cake:
            print("".join(row3))

