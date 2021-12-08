if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        c = int(input())
        b = list(map(int, input().split()))
        if b[0] == 0 or b[-1] == 0:
            print("Case #{}: IMPOSSIBLE".format(t))
            continue

        destCol = [-1 for _ in range(c)]
        curCol = 0
        for i, b_i in enumerate(b):
            for _ in range(b_i):
                destCol[curCol] = i
                curCol += 1

        board = [[] for _ in range(c)]
        for col in range(1, c):
            if destCol[col] < col:
                for i in range(destCol[col] + 1, col + 1):
                    board[i].append('/')
            elif destCol[col] > col:
                for i in range(col, destCol[col]):
                    board[i].append('\\')

        height = max([len(col) for col in board]) + 1
        print("Case #{}: {}".format(t, height))

        for col in board:
            colLen = len(col)
            for _ in range(height - colLen):
                col.append('.')

        for row in range(height):
            for col in range(c):
                print(board[col][row], end='')
            print()