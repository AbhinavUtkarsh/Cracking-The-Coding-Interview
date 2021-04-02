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


def remove_dup(llist):
    buffer={}
    
    # traversing the list to add elements to the buffer
    pointer=llist.head
    prev=None
    while(pointer!=None):
        
        if pointer.data not in buffer:
            buffer[pointer.data]=1
            prev=pointer
        else:
            prev.next=pointer.next
            # buffer[pointer.data]+=1
        pointer=pointer.next
        


    return llist





ll=remove_dup(ll)
print("\nUPDATED")
ll.display()