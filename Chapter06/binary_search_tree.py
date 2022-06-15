class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    def inorder(self): 
        current = self.root_node 
        if current is None: 
            return 
        inorder(current.left_child) 
        print(current.data) 
        inorder(current.right_child)
        
                    
    def get_node_with_parent(self, data): 
        parent = None 
        current = self.root_node 
        if current is None: 
            return (parent, None) 
        while True: 
            if current.data == data: 
                return (parent, current) 
            elif current.data > data: 
                parent = current 
                current = current.left_child 
            else: 
                parent = current 
                current = current.right_child 
        return (parent, current) 
   

    def remove(self, data):  
        parent, node = self.get_node_with_parent(data)  
 
        if parent is None and node is None:  
            return False  
 
        # Get children count  
        children_count = 0  
 
        if node.left_child and node.right_child:  
            children_count = 2  
        elif (node.left_child is None) and (node.right_child is None):  
            children_count = 0  
        else:  
            children_count = 1  
        
        if children_count == 0:  
            if parent:  
                if parent.right_child is node:  
                    parent.right_child = None  
                else:  
                    parent.left_child = None  
            else:  
                self.root_node = None 
        elif children_count == 1:  
            next_node = None  
            if node.left_child:  
                next_node = node.left_child  
            else:  
                next_node = node.right_child  
 
            if parent:  
                if parent.left_child is node:  
                    parent.left_child = next_node  
                else:  
                    parent.right_child = next_node  
            else:  
                self.root_node = next_node  
        else:  
            parent_of_leftmost_node = node  
            leftmost_node = node.right_child  
            while leftmost_node.left_child:  
                parent_of_leftmost_node = leftmost_node  
                leftmost_node = leftmost_node.left_child  
            node.data = leftmost_node.data       
    
            if parent_of_leftmost_node.left_child == leftmost_node:  
                parent_of_leftmost_node.left_child = leftmost_node.right_child  
            else:  
                parent_of_leftmost_node.right_child = leftmost_node.right_child             
            
            
    
    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                print("Item not found")
                return None
            elif current.data is data:
                print("Item found", data)
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child

                
    def find_min(self):  
        current = self.root_node  
        while current.left_child:  
            current = current.left_child  
        return current.data          
    
    
    def find_max(self):  
        current = self.root_node  
        while current.right_child:  
            current = current.right_child  
        return current.data  
      
      
      
tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)

tree.inorder()

for i in range(1, 10):
    found = tree.search(i)
    print("{}: {}".format(i, found))
    
    
print(tree.find_min())   

print(tree.find_max())   
      
