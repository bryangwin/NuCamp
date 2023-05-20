class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        
    
class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.num_nodes = 0
        
    def size(self):
        return self.num_nodes
    
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.num_nodes += 1
        
    def dequeue(self):
        if self.head is None:
            return None
        
        dq_node_value = self.head.value
        self.head = self.head.next
        self.num_nodes -= 1
        return dq_node_value
    
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print("Pass" if q.size() == 3 else "Fail")