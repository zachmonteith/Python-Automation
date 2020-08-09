#Deque: double ended queue
#resembles stack AND queue, but you can add or remove from either front or back.
# order is SORT OF preserved

#need to add from front and rear
#remove from front and rear
# is empty?
# how many items?
# next up front and rear

#any data type that could go in a list can go in a deque
#still limited access, because you can only get head or tail not other nodes, as it were

#good approach for testing for palindrome

class Deque:
    @staticmethod
    def _empty_helper():
        print("no items in deque")
        return None

    def __init__(self):
        self.items = []

    def push_left(self, item):
        self.items.insert(0, item)

    def push_right(self, item):
        self.items.append(item)

    def pop_left(self):
        if self.is_empty():
            return Deque._empty_helper()
        return self.items.pop(0)

    def pop_right(self):
        if self.is_empty():
            return Deque._empty_helper()
        return self.items.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def peek_left(self):
        if self.is_empty():
            return Deque._empty_helper()
        return self.items[0]

    def peek_right(self):
        if self.is_empty():
            return Deque._empty_helper()
        return self.items[-1]

#challenge: using deque, write function that takes string as input and returns true if palindrome

def is_palindrome(string):
    #create deque and store all characters in it in order
    storage = Deque()
    for char in string:
        storage.push_right(char)
    while storage.size() >= 2:
        if storage.pop_left() != storage.pop_right():
            return False
    return True
    #remove characters from the other end of the deque, they should match the original string
