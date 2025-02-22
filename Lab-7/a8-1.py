class Node:
    def __init__(self, data=0, next=None):
        self.data=data
        self.next=next
        
class LL(Node):
    def ins(o, head, pos):
        if pos==1:
            o.next=head
            head=o
        else:
            temp=head
            while (pos>2):
                temp=temp.next
                pos-=1
            temp2=temp.next
            temp.next=o
            o.next=temp2
        return head
    def deln(head, pos):
        if pos==1:
            temp=head.next
            del head
            head = temp
        else:
            temp = head
            while pos>2:
                temp=temp.next
                pos-=1
            temp2 = temp.next
            temp.next = temp.next.next
            del temp2
        return head
    def display(head):
        temp=head
        el=[]
        while temp!=None:
            el.append(str(temp.data))
            temp=temp.next
        print('->'.join(el))



l1=Node(5)
head=l1
l2=Node(6)
l3=Node(7)
l4=Node(8)

l1.next=l2
l2.next=l3
l3.next=l4

print("Cureent list: ")
LL.display(head)

user=True
while user:
    u = int(input(''''Enter:
            1. Insert
            2. Delete
            3. Display
            4. Exit\n'''))
    match u:
        case 1:
            d=int(input("Enter data: "))
            p=int(input("Enter position: "))
            o=Node(d)
            head = LL.ins(o, head, p)
        case 2:
            p=int(input("Enter position: "))
            head = LL.deln(head, p)
        case 3:
            LL.display(head)
        case 4:
            user=False
        case _:
            print("Invalid Input")

