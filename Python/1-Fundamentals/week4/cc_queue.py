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
        
class IceCreamShop:
    def __init__(self, flavors) -> None:
        self.flavors = flavors
        self.orders = Queue()
        
    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("Sorry that flavor is not available.")
            return
        elif scoops >= 1 and scoops <= 3:
            print("Order created!")
        else:
            print("Our scoop only come in 1, 2 or 3.")
            return
        order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        self.orders.enqueue(order)
        
    def show_all_orders(self):
        print("\nAll pending Ice Cream Orders:")
        for item in self.orders.items:
            print(f"Customer: {item['customer']} -- Flavor: {item['flavor']} -- Scoops: {item['scoops']}")
            
            
    def next_order(self):
        print("\nNext Order Up!")
        item = self.orders.dequeue()
        print(f"Customer: {item['customer']} -- Flavor: {item['flavor']} -- Scoops: {item['scoops']}")
        
                    
shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()