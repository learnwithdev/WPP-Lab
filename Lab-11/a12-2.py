import pandas as pd

s = pd.Series (["X", "Y", "T", "Aaba", "Baca", "CABA", None, "bird", "horse", "dog"])
# print(s)

#Uppercase
print("Uppercase: ")
s_upper = pd.Series([s[i].upper() for i in range(len(s)) if s[i]!=None])
print(s_upper)
                #OR
# s_upper = s.str.upper()
# print(s_upper)

#Lowercase
print("\nLowercase: ")
s_lower = pd.Series([s[i].lower() for i in range(len(s)) if s[i]!=None])
print(s_lower)