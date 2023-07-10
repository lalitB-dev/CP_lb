class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None


class doublyLL:
    def __init__(self):
        self.head= None

    # traversing the dubly linked list in forward direction
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"---->",end=" ")
                n=n.nref
            print("\n")

    # traversing the doubly linked list in reverse direction
    def print_ll_reverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.pref

    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked list is not empty")

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
    
    # to insert the new node after a given node
    def add_after(self,data,x):
        if self.head is None:
            print("LL is empty!")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("data not founf in dll")
            else:
                new_node= Node(data)
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref=new_node
                n.nref=new_node
    
    # to insert the node before a given node
    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty!")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("data not founf in dll")
            else:
                new_node=Node(data)
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node
                n.pref=new_node



dll=doublyLL()
dll.add_begin(10)
dll.add_after(5,10)
dll.add_before(100,5)
dll.print_ll()
dll.print_ll_reverse()




            



                


                 




