from collections import Counter

if __name__ == '__main__':
    s = input()

    count = Counter(s)
    mostCommon = list(count.items())
    mostCommon = sorted(mostCommon, key=lambda tup: tup[0])
    mostCommon = sorted(mostCommon, key=lambda tup: tup[1], reverse=True)

    for itm in mostCommon[:3]:
        print(*itm)