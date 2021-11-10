class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None

        
class SinglyLinkedList:
    def __init__ (self):
        self.tail = None
        self.head = None
        
    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node 
            self.head = node
        else:
            self.tail = node 
            self.head = node

            
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.tail
while current:
    print(current.data)
    current = current.next
