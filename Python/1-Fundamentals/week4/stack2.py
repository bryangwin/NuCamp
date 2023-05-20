class Stack:
    def __init__(self) -> None:
        self.items = []
        
    def push(self, value):
        self.items.append(value)
        
    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

popper = stack.pop()

print("Pass" if stack.size() == 5 else "Fail")

print(popper)