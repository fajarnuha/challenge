#!/c/Python27/python
import sys

group = []
prev = None
for line in sys.stdin:
    age, name = line.strip().split('\t')
    age = int(age)
    if age != prev and prev != None:
        sorted(group)
        for di in group:
            for out in di:
                print '%s\t%s' %(out, di[out])
        group = []
    group.append({name: age})
    prev = age

sorted(group)
for di in group:
    for out in di:
        print '%s\t%s' %(out, di[out])
