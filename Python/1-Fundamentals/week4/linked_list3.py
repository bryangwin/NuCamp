class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
      
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print(f"There was nothing here and now there is {self.head.value}")
            return
        
        node = self.head
        while node.next is not None:
            node = node.next
            
        node.next = new_node
        print(f"Appended new Node with value: {node.next.value}")
        

l_list = LinkedList()
l_list.append("1st")
l_list.append("2nd")
l_list.append("3rd")
