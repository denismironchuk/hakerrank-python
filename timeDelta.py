from datetime import datetime
import calendar

def getTimeZoneInfo(tzData):
    sign = 1
    if (tzData[0] == '-'):
        sign = -1

    tzTime = int(tzData[1:])
    tzHour = tzTime // 100
    tzMin = tzTime % 100

    return (sign, tzHour, tzMin)

def getDateTimeStruct(inpt):
    day = int(inpt[0])
    month = monthNum[inpt[1]]
    year = int(inpt[2])

    hour, min, sec = map(int, inpt[3].split(':'))

    return (datetime(year, month, day, hour, min, sec), getTimeZoneInfo(inpt[4]))

if __name__ == '__main__':
    monthNum = {}
    for i in range(1, 13):
        monthNum[calendar.month_abbr[i]] = i

    for _ in range(int(input())):
        inpt1 = (input().split())[1:]
        d1 = getDateTimeStruct(inpt1)

        inpt2 = (input().split())[1:]
        d2 = getDateTimeStruct(inpt2)

        if (d1[0] > d2[0]):
            seconds = (d1[0] - d2[0]).total_seconds()
            d1Add = d1[1][0] * ((d1[1][1] * 3600) + (d1[1][2] * 60))
            d2Add = d2[1][0] * ((d2[1][1] * 3600) + (d2[1][2] * 60))
            seconds -= d1Add
            seconds += d2Add
            print(abs(int(seconds)))
        else:
            seconds = (d2[0] - d1[0]).total_seconds()
            d1Add = d2[1][0] * ((d2[1][1] * 3600) + (d2[1][2] * 60))
            d2Add = d1[1][0] * ((d1[1][1] * 3600) + (d1[1][2] * 60))
            seconds -= d1Add
            seconds += d2Add
            print(abs(int(seconds)))
