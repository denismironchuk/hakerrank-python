cnt = 0

for i1 in range(2, 51):
    for i2 in range(4, 51):
        for i3 in range(8, 51):
            for i4 in range(16, 51):
                for i5 in range(32, 51):
                    if (i5 >= i4 * 2 and i4 >= i3 * 2 and i3 >= i2 * 2 and i2 >= i1 * 2):
                        cnt+=1
print(cnt)