class Node:
    def __init__ (self, data = None, next = None, prev = None):
        self.data = data 
        self.next = next
        self.prev = prev
        
class DoublyLinkedList:
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
            
            
            
    def delete(self, data):
        # Delete a node from the list. 
        current = self.head 
        node_deleted = False 
        if current is None:       #List is empty
            print("List is empty")
        elif current.data == data:   #Item to be deleted is found at starting of list
            self.head.prev = None 
            node_deleted = True 
            self.head = current.next

        elif self.tail.data == data:   #Item to be deleted is found at the end of list.
            self.tail = self.tail.prev  
            self.tail.next = None 
            node_deleted = True 

        else: 
            while current:          #search item to be deleted, and delete that node
                if current.data == data: 
                    current.prev.next = current.next  
                    current.next.prev = current.prev 
                    node_deleted = True 
                current = current.next 
            if node_deleted == False:   #Item to be deleted is not found in the list
                print("Item not found")
        if node_deleted: 
            self.count -= 1

            
            
            
#Code to create for a doubly linked list
words = DoublyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')
current = words.head
while current:
    print(current.data)
    current = current.next
    
    
words.delete('ham') 
current = words.head
while current:
    print(current.data)
    current = current.next
    

words.delete('spam')
current = words.head
while current:
    print(current.data)
    current = current.next
