a = int(input())
b = int(input())

l = [i for i in range(a,b+1)]

max=a^a
for i in range(len(l)):
    p=l[i]
    for j in range(i,len(l)):
        q=l[j]
        xor=p^q
        if xor>=max:
            max=xor
print(max)
