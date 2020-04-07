prob = 8 / 9
prob2 = 1 / 9
exp = 0;
for i in range(1,10000000):
    exp += i * prob2 * (prob ** (i - 1))
    print(exp)