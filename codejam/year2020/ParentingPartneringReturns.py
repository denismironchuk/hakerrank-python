if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n = int(input())
        activities = [(index, start, end) for index, start, end in [[i] + list(map(int, input().split())) for i in range(n)]]

        timeMoments = []
        for index, start, end in activities:
            timeMoments.append((index, start, 1))
            timeMoments.append((index, end, 0))

        timeMoments.sort(key=lambda m : m[2])
        timeMoments.sort(key=lambda m : m[1])

        assgn = {}
        workers = ['C', 'J']
        possible = True
        for index, time, isStart in timeMoments:
            if (isStart == 1):
                if (len(workers) == 0):
                    possible = False
                    break
                else:
                    assgn[index] = workers[0]
                    workers = workers[1:]
            else:
                workers.append(assgn[index])

        if (possible):
            print("Case #{}: {}".format(t, ''.join([assgn[i] for i in range(n)])))
        else:
            print("Case #{}: IMPOSSIBLE".format(t))





