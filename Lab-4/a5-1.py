uni=[]
t=int(input())

if t>=1 and t<=10:
    for j in range(t):
        uni.append(input())
    print("")
    # i=-1
    for j in range(len(uni)):
        s = uni[j]
        l = list(s)
        res = s
        n=0
        i = -1
        while (res!=res[::-1]):
            if res[i]!='a':
                l[i] = chr(ord(l[i])-1)
                res = ''.join(l)
                n+=1
            else:
                i-=1
        print(f"{n}")