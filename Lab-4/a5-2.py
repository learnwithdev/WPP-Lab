import math
roots = [i for i in range(31623)]
t = int(input())

l=[]
if t>=1 and t<=100:
    for i in range(t):
        l.append(list(map(int, input().split())))
        # print(l)
    print("")
    for j in range(len(l)):
        count=0
        k = l[j]
        for a in range(k[0], k[1]+1):
            if math.sqrt(a) in roots:
                count+=1 
        print(f"{count}")
