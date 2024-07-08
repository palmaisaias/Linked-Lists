from colorama import Fore, Back, Style

class Order():
    # this will handle the list of meals ordered, the table number, the 'next' requirement as well as tracking previous
    def __init__(self, meals, number):
        self.meals = meals
        self.number = number
        self.next = None
        self.prev = None

class Kitchen():

    def __init__(self):
        self.head = None
        self.tail = None
        
# --ADDS ORDER TO THE QUEUE
    def add_order(self, meals, number): 
        new_order = Order(meals, number)
        if self.head == None: 
            self.head = new_order 
            self.tail = new_order
        else: 
            self.tail.next = new_order
            new_order.prev = self.tail 
            self.tail = new_order

# --LETS YOU SEE ALL THE ORDERS...in a relatively creative way
    def view_orders(self): #O(n) Linear
        current = self.head
        if not current:
            print("No orders in the queue.")
            return

        print(Style.BRIGHT+"\nCurrent Orders:\n"+ Style.RESET_ALL)
        while current:
            clean_order = ', '.join(current.meals) # so the items dont print out in brackets
            print(f"{Fore.RED}Table {current.number}{Style.RESET_ALL}:")
            print(f"  Meals: {clean_order}")
            print("  ------------------------")
            current = current.next

# --'COOKS' ORDER THEREFORE REMOVES THE HEAD OF THE QUEUE AND MAKES THE 'NEXT' VALUE THE NEW HEAD
    def cook_order(self): 
        if self.head == None: #check if queue is empty
            return "Can't cook when there aint no orders, yo!"
        else:
            removed = self.head #remove the head
            self.head = self.head.next 
            if self.head: # checking if AFTER the update, the new value of self.head isnt None.
                self.head.prev = None  # update the new head's prev to None
            else:
                self.tail = None  # If the queue IS empty, update the tail to None
            clean_list = ', '.join(removed.meals)
            return f"{Fore.BLUE}{Style.BRIGHT}\nTable number {removed.number}, your order of {clean_list} is ready!!{Style.RESET_ALL}\n"
        
# --DELETES ORDER FOR A SPECIFIC TABLE NUMBER
    def delete_order(self, number):
        current = self.head
        while current:
            if current.number == number:
                if current.prev:  # if it's not the head
                    current.prev.next = current.next
                else:  # if it's the head
                    self.head = current.next
                if current.next:  # if it's not the tail
                    current.next.prev = current.prev
                else:  # if it's the tail
                    self.tail = current.prev
                return f"\n Order for table {number} has been TOSSED!"
            current = current.next
        return f"No order found for table {number}."

queue = Kitchen()

# SAMPLE TICKETS
queue.add_order(['Chicken Tenders', 'Fries', 'Leafy Salad'], 1)
queue.add_order(['Chicharrones', 'Salsa', 'Flower tortillas'], 2)
queue.add_order(['Coffee', 'Bagel'], 3)
queue.add_order(['Hotdog', 'Fries', 'Potato salad'], 4)


queue.view_orders()

print(queue.delete_order(3))

queue.view_orders()

print(queue.cook_order())

queue.view_orders()