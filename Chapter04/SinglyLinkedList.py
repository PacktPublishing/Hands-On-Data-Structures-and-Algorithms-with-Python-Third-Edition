class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None

    
class SinglyLinkedList:
    def __init__ (self):
        self.head = None
        self.size = 0
        
    def append(self, data):
        # Encapsulate the data in a Node 
        node = Node(data)
        if self.head is None:
            self.head = node    
        else: 
            current = self.head 
            while current.next:
                current = current.next 
            current.next = node 
            
            
            
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.head
while current:
    print(current.data)
    current = current.next
