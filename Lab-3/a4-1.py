n = int(input("Enter a number: "))
d_root=str(n)
flag = True
while flag:
    sum=0
    for i in range(len(d_root)):
        sum+=int(d_root[i])
    d_root=str(sum)
    if sum<10:
        flag=False

print(d_root)
