if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n = int(input())
        d = list(map(int, input().split()))

        leftPointer = 0
        rightPointer = len(d) - 1
        maxValue = 0
        res = 0

        while (leftPointer <= rightPointer):
            if (d[leftPointer] < d[rightPointer]):
                if (d[leftPointer] >= maxValue):
                    res+=1
                    maxValue = d[leftPointer]
                leftPointer+=1
            else:
                if (d[rightPointer] >= maxValue):
                    res+=1
                    maxValue = d[rightPointer]
                rightPointer-=1

        print("Case #{}: {}".format(t, res))