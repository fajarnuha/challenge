#!/c/Python27/python
import sys
for line in sys.stdin:
    name, age = line.strip().split()
    print(age + '\t' + name)
