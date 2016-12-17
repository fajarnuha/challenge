sizeA , MAX_DIFF = raw_input().split()
sizeA = int(sizeA)
MAX_DIFF = int(MAX_DIFF)

A = [];
for i in range(sizeA):
    A.append(input())

#sort the array
B = sorted(A)
INPUT_DIFF = B[sizeA-1] - B[0]

#distribute the difference to the biggest and smallest
DIFF = INPUT_DIFF - MAX_DIFF
ldiff = DIFF/2
rdiff = DIFF-ldiff
B[0] = B[0] + ldiff
B[sizeA-1] = B[sizeA-1] - rdiff

#substract the rest
cost = ldiff**2 + rdiff**2
i,j = sizeA-2,1
while B[i]>B[sizeA-1]:
    cost += (B[sizeA-1] - B[i])**2
    B[i] = B[sizeA-1]
    i=i-1
while B[j]<B[0]:
    cost += (B[0] - B[j])**2
    B[j] = B[0]
    j=j+1

print cost
