t = int(input())

if t<=15 and t>=1:
    N=[]
    for i in range(t):
        n=int(input())
        if n>=0 and n<=10**10:
            N.append(n)

    print("")
    for i in N:
        count=0
        i = str(i)
        for j in range(len(i)):
            if int(i)%int(i[j])==0:
                count+=1
        print(count)
