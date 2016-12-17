import random
total = 0
for i in range(100):
    s = 0
    for j in range(10000):
        s += random.randint(1,6)
    print s
    if (s > 34500 and s < 35500):
        total += 1
print total
