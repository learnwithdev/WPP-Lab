class Bank:
    def __init__(self, acc, bal):
        self.acc=acc
        self.bal=bal
    def withdraw(self, amt):
        self.bal-=amt
        return f"Remaining Balance: {self.bal}"
    def deposit(self, amt):
        self.bal+=amt
        return f"Total Balance: {self.bal}"
    def display(self):
        print(f"Acc. Number: {self.acc}")
        print(f"Balance: {self.bal}")

b1=Bank(123456, 500)
b2=Bank(123210, 1000)
b3=Bank(987654, 300)
user_acc={"Dev":b1, "Mark":b2, "Andrew":b3}

user=True

while user:
    name=input("Enter account name to proceed: ")
    
    op=int(input('''Enter:
                 1. Withdraw
                 2.Deposit
                 3. Display'''))
    
    match op:
        case 1:
            amt = int(input("Enter amount: "))
            user_acc[name].withdraw(amt)
            user = input("Enter 'q' to quit: ")
            if user=='q':
                user=False
        case 2:
            amt = int(input("Enter amount: "))
            user_acc[name].deposit(amt)
            user = input("Enter 'q' to quit: ")
            if user=='q':
                user=False
        case 3:
            user_acc[name].display()
            user = input("Enter 'q' to quit: ")
            if user=='q':
                user=False
        case _:
            print("Invalid Entry")
            user = input("Enter 'q' to quit: ")
            if user=='q':
               user=False
        
