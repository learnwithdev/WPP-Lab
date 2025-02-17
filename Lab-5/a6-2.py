t=int(input("enter the no.of test cases:"))
if(t>=0 and t<=10):
    for i in range(0,t+1):
        k=int(input("enter cutting variable k:"))
        if(k>=2 and k<=10**7):
            if(k%2!=0):
                print(f"the silvia could get {(k//2)*((k//2)+1)}chocolates")
            else:
                print(f"the silvia could get {(k//2)**2} chocalates")
        else:
            print("invalid input")