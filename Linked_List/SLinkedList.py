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

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def delete_node(self, node):
        if node == self.head:
            self.head = node.next
        curr = self.head.next
        prev = self.head
        while curr is not None:
            if curr == node:
                prev.next = curr.next
            curr = curr.next
            prev = prev.next

    def size(self):
        count = 0;
        curr = self.head
        while curr is not None:
            count += 1
        return count
    def insert_at(self, new_data, prev):
        new_node = Node(new_data)
        if prev is None:
            return f'Node doesnt exist. Linked list size({self.size()})'
        new_node.next = prev.next
        prev.next = new_node
    
    def clear_linked_list(self):
        self.head = None  

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

n6 = Node('Csharon Baby girl')
print('-------------------')
list1.add_node('n6')
list1.listprint()
print('')
list1.delete_node(n4)
list1.listprint()

print('')
list1.insert_at('Joe',list1.head)
list1.listprint()
list1.insert_at('Seattle',n5)
list1.listprint()
print('-------------------')
