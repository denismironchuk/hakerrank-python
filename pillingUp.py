from collections import deque

def popMax(d):
    if (d[0] > d[-1]):
        return d.popleft()
    else:
        return d.pop()

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        d = deque(map(int, input().split()))

        prev = popMax(d)

        while (len(d) != 0):
            next = popMax(d)
            if (next > prev):
                break
            else:
                prev = next

        if (len(d) == 0):
            print("Yes")
        else:
            print("No")


