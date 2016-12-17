import random

count = 0

for i in range(100000):
    c = []
    for j in range(8):
        c.append(random.randint(1,6))
    c = sorted(c)
    if sum(c[-4:]) == 24:
        count += 1

print count/100000.0
