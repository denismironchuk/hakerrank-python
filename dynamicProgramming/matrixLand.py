from random import randrange

def maxSumTrivial(lst):
    return max([(sum(lst[i:j]), (i, j)) for i in range(0, len(lst)) for j in range(i + 1, len(lst) + 1)], key=lambda tup: tup[0])

def maxSumOptimal(lst, resLst):
    if (len(lst) == 1):
        resLst += [lst[0]]
        return lst[0]

    prevMax = maxSumOptimal(lst[1:], resLst)
    res = max(lst[0], prevMax + lst[0])
    resLst += [res]
    return res

def maxSumOptimalNoRecur(lst):
    #resLst = [lst[-1]]
    #for i in range(len(lst) - 2, -1, -1):
    #    prevMax = resLst[-1]
    #    res = max(lst[i], prevMax + lst[i])
    #    resLst += [res]

    #return resLst

    lst = lst[::-1]
    res = [lst[0]]
    for v in lst[1:]:
        maxPrev = res[-1]
        res += [max(v, v + maxPrev)]

    return res[::-1]

while (True):
    lst = [randrange(-100, 100) for i in range(100)]
    print(lst)
    maxSum = maxSumTrivial(lst)
    print(maxSum)

    start, end = maxSum[1]
    maxSubList = lst[start:end]
    resTriv = sum(maxSubList)

    resLst = maxSumOptimalNoRecur(lst)
    resOpt = max(resLst)
    print(resOpt)

    if (resOpt != resTriv):
        raise RuntimeError("blablabla")

