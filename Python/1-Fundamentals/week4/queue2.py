class Queue:
    def __init__(self) -> None:
        self.items = []
        
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)
    
    def show_queue(self):
        print(self.items)
        
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.dequeue()

print("Pass" if q.size() == 3 else "Fail")

q.show_queue()