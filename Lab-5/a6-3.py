s = input()
l = [ord(i) for i in s]
l=l[::-1]
count=0
for m,k in enumerate(l):
    temp = k
    for j,i in enumerate(l):
        if i>temp and j!=len(l)-1:
            l[m]=i
            l[j]=temp
            count+=1
            break
    if count!=0:
        break
l = [chr(i) for i in l]
print(''.join(l[::-1]))