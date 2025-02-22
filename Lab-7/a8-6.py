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
user=True
while user:
    op=int(input('''Enter:
                 1. Withdraw
                 2.Deposit
                 3. Display'''))
    
    match op:
        case 1:
            amt = int(input("Enter amount: "))
            b1.withdraw(amt)
            user = input("Enter 'q' to quit: ")
            if user=='q':
                user=False
        case 2:
            amt = int(input("Enter amount: "))
            b1.deposit(amt)
            user = input("Enter 'q' to quit: ")
            if user=='q':
                user=False
        case 3:
            b1.display()
            user = input("Enter 'q' to quit: ")
            if user=='q':
                user=False
        case _:
            print("Invalid Entry")
            user = input("Enter 'q' to quit: ")
            if user=='q':
               user=False
        
