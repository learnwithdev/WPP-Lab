import random

l1 = [random.randint(0,1) for i in range(0,10)]
count = 0
max1 = sec_max = 0
l2 = []
for j in range(len(l1)):
    if l1[j]==0:
        count+=1
        # max=count
    else:
        max1 = count
        if max1!=0:
            l2.append((max1))
        count=0
print(l1)
print(f"0 has appeared {max(l2)} times in a row")
