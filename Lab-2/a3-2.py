product = {}

flag=True
while flag:
    p = input("Enter a product to add: ")
    v = int(input("Enter it's price: "))
    product[p] = v
    user = input("\nEnter 'q' if exit otherwise any other letter: \n\n")
    if user=='q':
        flag=False

flag=True
while flag:
    name = input("Enter product: ")
    if name in product:
        print(f"Price: {product[name]}")
    else:
        print("Product not available")
    user = input("\nEnter 'q' if exit otherwise any other letter: \n\n")
    if user=='q':
        flag=False
print("Thanks for using our program!")
    
    