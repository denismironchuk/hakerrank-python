class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Line(object):
    def __init__(self, p1, p2, A, B):
        self.p1 = p1
        self.p2 = p2
        self.A = A
        self.B = B
        if p1.x != p2.x:
            self.sign = 1 if p2.x > p1.x else -1
            self.k = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
            self.b = self.p1.y - self.k * self.p1.x

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        n, w, h = map(int, input().split())
        p, q, r, s = map(int, input().split())

        S = abs(p * s - q * r) / 2
        pointsX = []
        pointXLines = {}

        for _ in range(n):
            x, y, a, b = map(int, input().split())
            p1 = Point(x, y)
            p2 = Point(x + p, y + q)
            p3 = Point(x + r, y + s)

            if p1.x not in pointXLines:
                pointsX.append(p1.x)
                pointXLines[p1.x] = []
            if p2.x not in pointXLines:
                pointsX.append(p2.x)
                pointXLines[p2.x] = []
            if p3.x not in pointXLines:
                pointsX.append(p3.x)
                pointXLines[p3.x] = []

            line1 = Line(p1, p2, a, b)
            line2 = Line(p2, p3, a, b)
            line3 = Line(p3, p1, a, b)

            if line1.p1.x != line1.p2.x:
                pointXLines[p1.x].append(line1)
                pointXLines[p2.x].append(line1)

            if line2.p1.x != line2.p2.x:
                pointXLines[p2.x].append(line2)
                pointXLines[p3.x].append(line2)

            if line3.p1.x != line3.p2.x:
                pointXLines[p1.x].append(line3)
                pointXLines[p3.x].append(line3)

        pointsX.sort()

        segmentA = []
        segmentB = []

        currentLines = set()

        for i in range(len(pointsX) - 1):
            x1 = pointsX[i]
            x2 = pointsX[i + 1]
            for line in pointXLines[x1]:
                if line in currentLines:
                    currentLines.remove(line)
                else:
                    currentLines.add(line)

            segmentASum = 0
            segmentBSum = 0
            chisl = 0
            znam = 0
            for line in currentLines:
                segmentASum += line.sign * line.A * (line.k * (x1 + x2) + 2 * line.b) * (x2 - x1)
                segmentBSum += line.sign * line.B * (line.k * (x1 + x2) + 2 * line.b) * (x2 - x1)

            segmentASum /= 2 * S
            segmentBSum /= 2 * S
            segmentA.append(segmentASum)
            segmentB.append(segmentBSum)

        leftSums = [0]
        for seg in segmentA:
            leftSums.append(leftSums[-1] + seg)

        rightSums = [0 for _ in range(len(segmentB) + 1)]
        for i in range(len(segmentB) - 1, -1, -1):
            rightSums[i] = rightSums[i + 1] + segmentB[i]

        candidates = []

        for i in range(len(pointsX)):
            candidates.append(abs(rightSums[i] - leftSums[i]))

        currentLines = set()

        for i in range(len(pointsX) - 1):
            x1 = pointsX[i]
            x2 = pointsX[i + 1]
            for line in pointXLines[x1]:
                if line in currentLines:
                    currentLines.remove(line)
                else:
                    currentLines.add(line)

            chisl = 0
            znam = 0
            for line in currentLines:
                chisl -= (line.A + line.B) * line.sign * line.b
                znam += (line.A + line.B) * line.sign * line.k

            if znam != 0:
                extremum = chisl / znam
                if extremum > x1 and extremum < x2:
                    extremumValue = 0
                    for line in currentLines:
                        extremumValue += line.sign * line.A * (line.k * (x1 + extremum) + 2 * line.b) * (extremum - x1)
                        extremumValue -= line.sign * line.B * (line.k * (extremum + x2) + 2 * line.b) * (x2 - extremum)

                    extremumValue /= 2 * S
                    extremumValue += rightSums[i]
                    extremumValue -= leftSums[i + 1]

                    candidates.append(abs(extremumValue))

        candidates.sort()
        print(candidates[0])
