def fact(n):
    if n==1:
        return 1
    else:
        factorial=n*fact(n-1)
        return factorial
print(f"The factorial of 6 is: {fact(6)}")