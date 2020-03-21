from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    purch = OrderedDict()
    for _ in range(n):
        intList = input().split()
        price = int(intList[-1])
        name = ' '.join(intList[:-1])

        if (name not in purch):
            purch[name] = price
        else:
            purch[name] += price

    for item, price in purch.items():
        print(item, price)