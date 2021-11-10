class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0
        
    def empty(self):
        return self.items == []
   
    def enqueue(self, data):
        self.items.insert(0, data)    # Always insert items at index 0 
        self.size += 1          # increment the size of the queue by 1 
    
    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data
    
    def size1(self):
        # print(self.size)
        return self.size


q= ListQueue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue('cat')
q.enqueue('monday')


a= q.size1()
print(a)
