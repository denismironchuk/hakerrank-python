if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n = int(input())
        heights = list(map(int, input().split()))
        res = 0

        for i in range(1, len(heights) - 1):
            if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
                res += 1

        print("Case #{}: {}".format(t, res))