fib = [0,1]
# sum=0
t = int(input())
if t>=1 and t<=10**5:
    for i in range(t):
        sum=0
        user = int(input())
        while sum<user and user<10**10:
            sum=fib[-2]+fib[-1]
            fib.append(sum)
        if user in fib:
            print('IsFibo')
        else:
            print("IsNotFibo")
        # print(fib)