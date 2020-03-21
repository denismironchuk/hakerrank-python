from collections import defaultdict

if __name__ == '__main__':
    dict = defaultdict(list)
    n, m = map(int, input().split())
    for index in range(1, n + 1):
        elmt = input()
        dict[elmt].append(index)

    for _ in range(m):
        arr = dict[input()]
        if (len(arr) == 0):
            print(-1)
        else:
            print(*arr)
