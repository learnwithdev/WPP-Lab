import math

l1 = [[1,1,1],[2,1,2],[1,3,3],[3,2,1]]

for i in range(len(l1)):
    dict={}
    for j in range(len(l1)):
        if i==j:
            continue
        else:
            v = math.dist(l1[i], l1[j])
            k = tuple(l1[j])
            dict[k] = v
    # print(dict)
    min_v=list(dict.values())[0]
    min=list(dict.keys())[0]
    for k,v in dict.items():
        if dict[k]<min_v:
            min=k
            min_v=dict[min]
    print(f"Point {l1[i]} is closest to {min}: {min_v}\n")

    