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
        # if temp>i and j==len(s)-1:
        #     l[0] = l[j]
        #     l[j] = temp
        # else:
        #     count+=1
l = [chr(i) for i in l]
print(''.join(l[::-1]))