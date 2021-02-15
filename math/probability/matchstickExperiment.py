from random import random

class Side():
    def __init__(self):
        self.removed = False
        self.processed = False

    def remove(self):
        self.removed = True

class Cell():
    def __init__(self):
        self.leftSide = None
        self.rightSide = None
        self.upSide = None
        self.downSide = None

        self.leftCell = None
        self.rightCell = None
        self.upCell = None
        self.downCell = None

    def initSides(self):
        if (not self.leftSide):
            self.leftSide = Side()
            if (self.leftCell):
                self.leftCell.rightSide = self.leftSide

        if (not self.rightSide):
            self.rightSide = Side()
            if (self.rightCell):
                self.rightCell.leftSide = self.rightSide

        if (not self.upSide):
            self.upSide = Side()
            if (self.upCell):
                self.upCell.downSide = self.upSide

        if (not self.downSide):
            self.downSide = Side()
            if (self.downCell):
                self.downCell.upSide = self.downSide

    def getSides(self):
        return list(filter(lambda side: side != None, [self.downSide, self.upSide, self.leftSide, self.rightSide]))

    def isFullCell(self):
        return not self.leftSide.removed and not self.rightSide.removed and not self.upSide.removed and not self.downSide.removed

    def onlyNoDown(self):
        return not self.leftSide.removed and not self.rightSide.removed and not self.upSide.removed and self.downSide.removed

    def onlyNoUp(self):
        return not self.leftSide.removed and not self.rightSide.removed and self.upSide.removed and not self.downSide.removed

    def onlyNoRight(self):
        return not self.leftSide.removed and self.rightSide.removed and not self.upSide.removed and not self.downSide.removed

    def onlyNoLeft(self):
        return self.leftSide.removed and not self.rightSide.removed and not self.upSide.removed and not self.downSide.removed

    def cells2Right(self):
        if (self.rightCell):
            return self.onlyNoRight() and self.rightCell.onlyNoLeft()
        else:
            return False

    def cells2Down(self):
        if (self.downCell):
            return self.onlyNoDown() and self.downCell.onlyNoUp()
        else:
            return False

if __name__ == '__main__':
    rows = 10
    cols = 10
    removeProb = 0.4

    avgFullCells = 0


    for itr in range(100000):
        cells = [[Cell() for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if (row != 0):
                    cells[row][col].upCell = cells[row - 1][col]

                if (row != rows - 1):
                    cells[row][col].downCell = cells[row + 1][col]

                if (col != 0):
                    cells[row][col].leftCell = cells[row][col - 1]

                if (col != cols - 1):
                    cells[row][col].rightCell = cells[row][col + 1]

                cells[row][col].initSides()

        for row in range(rows):
            for col in range(cols):
                for side in cells[row][col].getSides():
                    if not side.processed:
                        if random() < removeProb:
                            side.removed = True
                        side.processed = True

        fullCellsCnt = 0

        for row in range(rows):
            for col in range(cols):
                if cells[row][col].isFullCell():
                    fullCellsCnt += 1

                if cells[row][col].cells2Down():
                    fullCellsCnt += 1

                if cells[row][col].cells2Right():
                    fullCellsCnt += 1

        avgFullCells = (avgFullCells * itr + fullCellsCnt) / (itr + 1)

        if (itr % 1000 == 0):
            print(avgFullCells)