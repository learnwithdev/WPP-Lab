s = {i for i in range(1,10001)}
# print(s)
s0 = {i for i in s if i%5==0}
s1 = {i for i in s if i%5==1}
s2 = {i for i in s if i%5==2}
s3 = {i for i in s if i%5==3}
s4 = {i for i in s if i%5==4}
print(f'''The equivalence classes are: 
        [0]: {list(s0)[:7]}...
        [1]: {list(s1)[:7]}...
        [2]: {list(s2)[:7]}...
        [3]: {list(s3)[:7]}...
        [4]: {list(s4)[:7]}...''')

sCheck = s0.union(s1,s2,s3,s4)
print("Original Set==Union of all classes:", s==sCheck)