#With time-complexity: O(n)
price = [60,70,80,100,90,75,80,120]
span=[]

count=0
j=0
i=0

while i<len(price):
    if i==0:
        count+=1
        span.append(count)
        i+=1
        count=0
    else:
        if j<=i and price[i]>=price[j]:
            count+=1
            j+=1
        else: 
            if count !=0 and j>i:
                i=j
                j=0
                span.append(count)
                count=0
            else:
                count=0
                j+=1
print(span)
