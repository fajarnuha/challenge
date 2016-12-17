#!/c/Python27/python
import random,string

for i in range(1000000):
    line = ''.join(random.choice(string.lowercase) for i in range(6))
    line += " " + str(random.randint(0,1000000))
    print line
