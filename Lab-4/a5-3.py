letters = 'abcdefghijklmnopqrstuvwxyz'
# s = "the quick brown fox jumps over a lazy dog"
s = input()
i=0
for letter in letters:
    if letter not in s:
        i+=1
if i!=0:
    print("Not Pangram")
else:
    print("Pangram")