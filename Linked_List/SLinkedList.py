# create class for node objects
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create class to link nodes together
class SLinkedList:
    def __init__(self):
        self.head = None
        
    def listprint(self):
        curr = self.head
        count = 1
        while curr is not None:
            print(f'{count}: {curr.data}')
            curr = curr.next
            count += 1

# create linkedlist and add nodes, print to console
list1 = SLinkedList()
list1.head = Node('Erik')

n2 = Node('Messi')
n3 = Node('Neymar')
n4 = Node('Ronaldo')
n5 = Node('Rudiaz')

list1.head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

list1.listprint()

