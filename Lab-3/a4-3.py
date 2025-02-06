t = int(input())
N=[]
height=1
if t>=1 and t<=10:
    for i in range(t):
        n = int(input())
        if n >=0 and n<=60:
            N.append(n)    
    print("")
    k=0
    while k<len(N):
        height=1
        for j in range(N[k]):
            if j%2==0:
                height*=2
            else:
                height+=1
        print(height)
        k+=1
