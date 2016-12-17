import random

stats = {str(x+1):0 for x in range(6)}

for i in range(1000000):
    store = set()
    for i in range(6):
        t = random.randint(1,6)
        store.add(t)

    stats[str(len(store))] += 1

print stats
