#stack: recursion?
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """accepts an item as a parameter and appends it to the end of list, returns nothing

        the runtime for this method is constant (O(1)).
        """
        self.items.append(item)

    def pop(self):
        """removes and returns the last item from the list aka top item of stack in constant time"""
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """this method returns last item in list, aka top of stack.  constant time bc indexing in list is constant yo
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """returns length of list that represents stack.  constant time."""
        return len(self.items)

    def is_empty(self):
        '''returns boolean of whether stack is empty, in constant time'''
        if self.items:
            return False
        return True

def match_symbols(string):
    symbol_pairs = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    openers = symbol_pairs.keys()
    match_stack = Stack()

    for char in string:
        if char in openers:
            match_stack.push(char)
        elif symbol_pairs[match_stack.peek()] == char:
            match_stack.pop()
        else:
            return False
    return match_stack.is_empty()
