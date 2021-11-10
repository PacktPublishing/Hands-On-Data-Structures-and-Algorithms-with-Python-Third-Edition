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
            
    def delete_First_node (self): 
        current = self.tail  
        if current == self.tail:
            self.tail = current.next        
          
    def delete_last_node (self): 
        current = self.tail 
        prev = self.tail 
        while current:
            if current.next == None:
                prev.next = current.next 
                self.size -= 1
            prev = current
            current = current.next
            

    def delete(self, data): 
        current = self.tail 
        prev = self.tail 
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next 
                else:
                    prev.next = current.next 
                self.size -= 1
                return
            prev = current
            current = current.next
            
            
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')


words.delete_last_node()

current = words.tail
while current:
    print(current.data)
    current = current.next
    
    
    
words.delete('ham')
current = words.tail
while current:
    print(current.data)
    current = current.next
    
    
