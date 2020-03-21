from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    Row = namedtuple('Row', input().split())
    sum = 0
    for _ in range(n):
        sum += int(Row(*(input().split())).MARKS)

    print(round(sum / n, 2))