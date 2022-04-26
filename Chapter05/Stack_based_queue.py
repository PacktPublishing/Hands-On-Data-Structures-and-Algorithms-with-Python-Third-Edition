class Queue:  
    def __init__(self):  
        self.Stack1 = []  
        self.Stack2 = []  
                
    def enqueue(self, data):  
        self.Stack1.append(data)
        
        

        def dequeue(self):   
        if not self.Stack2:  
            while self.Stack1:  
                self.Stack2.append(self.Stack1.pop())  
        if not self.Stack2:
            print("No element to dequeue")
            return
        return self.Stack2.pop()  
      
      
queue = Queue()  
queue.enqueue(5)  
queue.enqueue(6)  
queue.enqueue(7)  
print(queue.Stack1)  

queue.dequeue()  
print(queue.Stack1)  
print(queue.Stack2)  
queue.dequeue()  
print(queue.Stack2)        
