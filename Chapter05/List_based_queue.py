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
        


q = ListQueue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.items)
#Queue is full
#[20, 30, 40]


data = q.dequeue()
print(data)
print(q.items)
#20
#[30, 40]


a = q.size1()
print(a)
