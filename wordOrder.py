from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    dict = OrderedDict()

    for _ in range(n):
        word = input()
        if (word not in dict):
            dict[word] = 1
        else:
            dict[word] += 1

    print(len(dict.keys()))
    print(*(dict.values()))