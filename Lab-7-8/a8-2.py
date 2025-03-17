from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()
    def enqueue(self, data):
        self.q.append(data)
    def dequeue(self):
        return self.q.popleft()
    def peek(self):
        return self.q[0] 

q1 = Queue()
print("Queue is initially Empty")
user = True
while user:
    u = int(input('''Enter:
                    1. Enqueue
                    2. Dequeue
                    3. Peek
                    4. Exit\n'''))
    match u:
        case 1:
            d = int(input("Enter data: "))
            q1.enqueue(d)
        case 2:
            print(q1.dequeue())
        case 3:
            print(q1.peek())
        case 4:
            user=False
        case _:
            print("Invald Input")
