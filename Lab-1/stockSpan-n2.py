#With time-complexity: O(n^2)
price = [60,70,80,100,90,75,80,120]
span=[]

count=0
j=0
i=len(price)-1

while i>=0:
    if i==0:
        count+=1
        span.append(count)
        i-=1
        count=0
    else:
        while j<=i:
            if price[j]<=price[i]:
                count+=1
            else:
                count=0
            j+=1
        span.append(count)
        count=j=0
        i-=1
span = span[::-1]
print(span)
