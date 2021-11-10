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
    
    def append_at_a_location(self, data, index): 
        current = self.tail 
        prev = self.tail 
        node = Node(data)
        count = 1
        while current:
            if count == index:        
                node.next = current 
                prev.next = node
                print(count)
                return
            elif index == 1:
                node.next = current
                self.tail = node
                return
            count += 1
            prev = current
            current = current.next       
            
            
            
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.tail
while current:
    print(current.data)
    current = current.next
    
    
    
words.append_at_a_location('new', 2)

current = words.tail
while current:
    print(current.data)
    current = current.next
    
    

