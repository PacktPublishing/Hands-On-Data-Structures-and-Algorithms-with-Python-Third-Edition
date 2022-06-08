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
            
    def delete_first_node (self): 
        current = self.head  
        if self.head is None:
            print("No data element to delete")
        elif current == self.head:
            self.head = current.next
            
          
    def delete_last_node (self): 
        current = self.head 
        prev = self.head
        while current:
            if current.next is None:
                prev.next = current.next 
                self.size -= 1
            prev = current
            current = current.next
            

    def delete(self, data): 
        current = self.head 
        prev = self.head 
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next 
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

words.delete_first_node()

current = words.head
while current:
    print(current.data)
    current = current.next


    
words.delete_last_node()

current = words.head
while current:
    print(current.data)
    current = current.next
    
    
    
words.delete('ham')
current = words.head
while current:
    print(current.data)
    current = current.next
    
    
