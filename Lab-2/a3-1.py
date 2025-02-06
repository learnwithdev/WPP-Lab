s = "Heisenberg"
o=""
for i in range(len(s)):
    if i%2!=0:
        o+=s[i].upper()
    else:
        o+=s[i]
print(o)
