class ListQueue:  
    def __init__(self):  
        self.items = []  
        self.front = self.rear = 0
        self.size = 3  # maximum capacity of the queue
        
    def enqueue(self, data):  
        if self.size == self.rear:
            print("\nQueue is full")
        else:   
            self.items.append(data)  
            self.rear += 1
            
        
        
    def dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            data = self.items.pop(0)    # delete the item from front end of the queue            
            self.rear -= 1
            return data 
        


q= ListQueue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue('cat')
q.enqueue('monday')


a= q.size1()
print(a)
