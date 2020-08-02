if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        s = input()
        stat = {'a': 0, 'b': 0, 'c': 0}
        for c in s:
            stat[c] += 1

        if (stat['a'] == len(s) or stat['b'] == len(s) or stat['c'] == len(s)):
            print(len(s))
        elif (stat['a'] % 2 == stat['b'] % 2 and stat['b'] % 2 == stat['c'] % 2):
            print(2)
        else:
            print(1)