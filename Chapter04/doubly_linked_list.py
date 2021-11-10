class Node(object):
    def __init__ (self, data = None, next = None, prev = None):
        self.data = data 
        self.next = next
        self.prev = prev
        
class DoublyLinkedList(object):
    def __init__ (self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def append(self, data):
        #Append an item to the list.   
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail 
            self.tail.next = new_node 
            self.tail = new_node
            self.count += 1
            
            
    def append_at_start(self, data):
        # Append an item at beginning to the list. 
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node
            self.count += 1
            
     def append_at_a_location(self, data): 
        current = self.head 
        prev = self.head 
        new_node = Node(data, None, None)
        while current:
            if current.data == data:
                new_node.prev = prev
                new_node.next = current
                prev.next = new_node
                current.prev = new_node
                self.count += 1
            prev = current
            current = current.next            



words = DoublyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.head
while current:
    print(current.data)
    current = current.next
    
    
words.append_at_a_location('ham')
current = words.head
while current:
    print(current.data)
    current = current.next
