class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        node=Node(data,None)
        if self.head==None:
            self.head=node
        else:
            itr=self.head
            while(itr.next):
                itr=itr.next
            itr.next=node

    def display(self):

        if self.head is None:
            print("Empty Linked List")
            return
        else:
            itr=self.head
            while(itr!=None):
                if itr.next==None:
                    print(str(itr.data) + "--> NULL",end=" ")
                else:
                    print(str(itr.data) + "--> ",end=" ")
                itr=itr.next

ll=LinkedList()
ll.insert_at_begining(5)
ll.insert_at_begining(15)
ll.insert_at_begining(54)
ll.insert_at_begining(12)
ll.insert_at_end(91)
ll.insert_at_end(88)
ll.insert_at_end(77)
ll.display()