from collections import defaultdict
Test = [{'test1':{'Dhoni':74, 'Kohli': 150}}, {'test2': {'Dhoni':29, 'Kohli':143}}]
res_dict = {}
dict1 = {}
mylist = ["Dhoni", "Kohli", "Sachin"]

# for i in range(0,2):
#     mylist.append(Test[i])

res_dict = {i: 0 for i in mylist}

for i in range(0,2):
    dict1 = Test[i]
    for k,v in dict1.items():
        res_dict["Dhoni"] += v["Dhoni"]
        res_dict["Kohli"] += v["Kohli"]
        res_dict["Sachin"] += v["Sachin"]
print(res_dict)

# for i in range(0,2):
#     dict1 = (Test[i].values())
#     print(dict(dict1))
    # l = list(dict1.keys())
    # for s in l:
    #     print(s)
#         if key=='Dhoni':
#             res_dict["Dhoni"] += value
#         elif key=='Kohli':
#             res_dict["Kohli"] += value
#         elif key=='Sachin':
#             res_dict["Sachin"] += value
# print(res_dict)
