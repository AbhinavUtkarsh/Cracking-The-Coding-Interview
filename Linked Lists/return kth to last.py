class Node:

    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:

    def __init__(self):
        self.head=None
    
    def add_at_beg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def display(self):

        if self.head==None:
            print("Linked List is empty")
        
        else:
            pointer=self.head
            while(pointer!=None):
                print(str(pointer.data) + "--> ", end=" ")
                pointer=pointer.next

ll=LinkedList()
ll.add_at_beg(1)
ll.add_at_beg(4)
ll.add_at_beg(5)
ll.add_at_beg(2)
ll.add_at_beg(3)
ll.add_at_beg(1)
ll.add_at_beg(4)
ll.add_at_beg(3)
ll.add_at_beg(11)
ll.add_at_beg(11)

ll.display()


def kth_last(llinked,k):

    # getting the length of the linked list


    n=0
    pointer=llinked.head
    while(pointer!=None):
        pointer=pointer.next
        n+=1

    counter=1
    pointer=llinked.head
    while(counter!=n-k+1):
        pointer=pointer.next
        counter+=1
    
    element=pointer.data

    return element




k=3
element=kth_last(ll,k)
print(f"\nThe {k}rd/th last element is: {element}")
