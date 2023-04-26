class DoubleNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def append(self, value):
        new_node = DoubleNode(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        
dlist = DoublyLinkedList()

dlist.append("James")

