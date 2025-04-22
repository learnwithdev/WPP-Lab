import numpy as np
import math

rng = np.random.default_rng(12345)
rints = rng.integers(low=-100, high=101, size=(10,2))
print(rints)
x, y = rints[:,0], rints[:,1]
# print(x)
r = np.sqrt(x**2) + np.sqrt(y**2)
p = []
for i in range(0,10):
    t = math.atan(y[i]/x[i])
    p.append([r[i], t])
    print(p[i])
    # p1 = r[i]*np.cos(t)
    # p2 = r[i]*np.sin(t)
    # p.append(complex(p1,p2))
# print(p)