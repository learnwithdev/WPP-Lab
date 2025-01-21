# Test = [{'test1':{'Dhoni':74, 'Kohli': 150}}, {'test2': {'Dhoni':29, 'Sachin':143}}]
Test = [{'Dhoni':74, 'Kohli': 150}, {'Dhoni':29, 'Sachin':167}]

dict1 = {}
mylist = ["Dhoni", "Kohli", "Sachin"]
res_dict = {i: 0 for i in mylist}

for i in range(0,2):
    dict1 = Test[i]
    if "Dhoni" in dict1:
        res_dict["Dhoni"] += dict1["Dhoni"]
    if "Kohli" in dict1:            
        res_dict["Kohli"] += dict1["Kohli"]
    if "Sachin" in dict1:
        res_dict["Sachin"] += dict1["Sachin"]
# print(res_dict)
nmax = "Dhoni"
rmax=res_dict[nmax]
for k,v in res_dict.items():
    if res_dict[k]>rmax:
        rmax = res_dict[k]
        nmax = k
print(f"{nmax} wins the Orange Cap for {rmax} runs.")
