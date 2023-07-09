class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    # traversing the linked list
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head

            while n is not None:
                print(n.data,"---->",end=" ")
                n=n.ref
    
# Insertion related operations:
# add elements in the beginning of a linked list
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    #add elements at the end of the linked list
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                 n=n.ref  
            n.ref=new_node
    
    def add_after(self,data,x):
        n=self.head
        while n is not None:
             if n.data==x:
                 break
             n=n.ref    
        if n is None:
            print("node is not present in th LL")
        else:
           new_node=Node(data)
           new_node.ref=n.ref
           n.ref=new_node    

    def add_before(self,data,x):
        if self.head is  None:
            print("Linked list is empty")
            return
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
               break
            n=n.ref
        
        if n.ref is None:
            print("node is not present in th LL")
        else:
           new_node=Node(data)
           new_node.ref=n.ref
           n.ref=new_node
    
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked list is not empty")

# Deletion related operations:
    def delete_begin(self):
        if self.head is None:
            print("Linked list is  empty")
        else:
            self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked list is  empty")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None


ll1=LinkedList()
ll1.add_begin(10)
ll1.delete_end()
ll1.print_ll()

    
    

