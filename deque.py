from collections import deque

if __name__ == '__main__':
    n = int(input())
    d = deque()

    commands = {
        'append': d.append,
        'pop': d.pop,
        'popleft': d.popleft,
        'appendleft':d.appendleft,
    }

    for _ in range(n):
        inpt = input().split()
        command = inpt[0]
        params = inpt[1:]
        commands[command](*params)

    print(*d)