def getTurnCandidates(turns, a, b, c):
    for h in range(12):
        for m in range(60):
            hNs = h * 60 * 60 * (10 ** 9)
            mNs = m * 60 * (10 ** 9)

            cand1 = (12 * a - b - 12 * hNs) / 11
            cand2 = (60 * b - c - 720 * mNs) / 59

            while cand1 < 0:
                cand1 += 12 * 60 * 60 * 10 ** 9

            while cand1 >= 12 * 60 * 60 * 10 ** 9:
                cand1 -= 12 * 60 * 60 * 10 ** 9

            while cand2 < 0:
                cand2 += 12 * 60 * 60 * 10 ** 9

            while cand2 >= 12 * 60 * 60 * 10 ** 9:
                cand2 -= 12 * 60 * 60 * 10 ** 9

            if cand1 == cand2:
                cand = cand1
                time = a - cand

                while time < 0:
                    time += 12 * 60 * 60 * 10 ** 9

                while time >= 12 * 60 * 60 * 10 ** 9:
                    time -= 12 * 60 * 60 * 10 ** 9

                turns.append(time)

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        a, b, c = map(int, input().split())
        turns = []
        getTurnCandidates(turns, a, b, c)
        getTurnCandidates(turns, a, c, b)
        getTurnCandidates(turns, b, a, c)
        getTurnCandidates(turns, b, c, a)
        getTurnCandidates(turns, c, a, b)
        getTurnCandidates(turns, c, b, a)

        turns.sort()
        time = turns[0]

        hours = int(time // (60 * 60 * 10 ** 9))
        time %= 60 * 60 * 10 ** 9
        minutes = int(time // (60 * 10 ** 9))
        time %= 60 * 10 ** 9
        seconds = int(time // (10 ** 9))
        nanoseconds = int(time % (10 ** 9))

        print("Case #{}: {} {} {} {}".format(t, hours, minutes, seconds, nanoseconds))
