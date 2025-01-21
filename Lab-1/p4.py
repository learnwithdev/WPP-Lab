a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"Values before Swapping: {a}, {b}")

a = a+b
b = a-b
a = a-b

print(f"Values after Swapping: {a}, {b}")