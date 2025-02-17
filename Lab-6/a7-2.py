import random

class RPS:
    def __init__(self, n):
        self.n = n #No. of Rounds
        self.l = ['rock', 'paper', 'scissors']
        self.uwin=0
        self.cwin=0

    def play(self):
        d = {'rock':'✊', 'paper':'🖐️', 'scissors':'✌️'}
        i=0
        while i<self.n:
            user=int(input('''Enter: 
                1. Rock
                2. Paper
                3. Scissors: '''))
            comp=random.choice(self.l)
            
            print(f"You: {d[self.l[user-1]]}   x   {d[comp]} :Them")
            if self.l[user-1]=='rock' and comp=='scissors':
                self.uwin+=1
                print(f"You won round {i+1}!")
            elif self.l[user-1]=='paper' and comp=='rock':
                self.uwin+=1
                print(f"You won round {i+1}!")
            elif self.l[user-1]=='scissors' and comp=='paper':
                self.uwin+=1
                print(f"You won round {i+1}!")
            elif self.l[user-1]==comp:
                print(f"Round {i+1}: Draw")
            else:
                self.cwin+=1
                print(f"Computer won round {i+1}")
            i+=1
    def results(self):
        if (self.uwin>self.cwin):
            print("\nYou won this game")
        elif (self.uwin==self.cwin):
            print("\nIt's a Draw!")
        else:
            print("\nComputer won this game")
u1 = RPS(5)
u1.play()
u1.results()


    