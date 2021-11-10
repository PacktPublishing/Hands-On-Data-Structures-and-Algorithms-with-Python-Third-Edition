class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__ (self):
        self.tail = None
        
    def append(self, data):
        # Encapsulate the data in a Node 
        node = Node(data)
        if self.tail == None:
            self.tail = node    
        else: 
            current = self.tail 
            while current.next:
                current = current.next 
            current.next = node
    
    def iter(self):
        current = self.tail 
        while current:
            val = current.data 
            current = current.next 
            yield val

            
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

for word in words.iter():
    print(word)
