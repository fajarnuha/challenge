import random

avg = []
for i in range(100000):
    rolls = 0
    con = True
    count = 0
    prev = None
    while(con):
        rolls += 1
        now = random.randint(1,6)
        if now == prev:
            count += 1
        else:
            count = 0
        if count == 2:
            con = False
        prev = now
    avg.append(rolls)

print sum(avg)
