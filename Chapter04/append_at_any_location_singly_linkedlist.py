class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__ (self):
        self.tail = None
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
        self.size += 1

    def append_at_a_location(self, data, index):  
        current = self.head  
        prev = self.head  
        node = Node(data) 
        count = 1 
        if index == 1:         
                node.next = current 
                self.head = node 
                self.size += 1
                print(count) 
                return
        else:
            while current:  
                if count == index: 
                    node.next = current  
                    prev.next = node
                    self.size += 1
                    return 
                count += 1 
                prev = current 
                current = current.next 
        if count < index: 
            print("The list has less number of elements") 


words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.head
while current:
    print(current.data)
    current = current.next

words.append_at_a_location('new', 2)

current = words.head
while current:
    print(current.data)
    current = current.next
    
    

