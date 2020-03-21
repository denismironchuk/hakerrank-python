from collections import Counter

if __name__ == '__main__':
    x = int(input())
    sizes = map(int, input().split())
    n = int(input())
    customers = [tuple(map(int, input().split())) for _ in range(n)]

    sizesCnt = Counter(sizes)

    totalPrice = 0

    for size, price in customers:
        if (sizesCnt[size] > 0):
            totalPrice += price
            sizesCnt[size] -= 1

    print(totalPrice)