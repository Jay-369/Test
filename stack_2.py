class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)


# Example usage
stack = Stack()

# Pushing elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())  # Output: 3
print("Stack peek:", stack.peek())  # Output: 3

# Popping elements from the stack
print("Popped item:", stack.pop())  # Output: 3
print("Popped item:", stack.pop())  # Output: 2

print("Stack size:", stack.size())  # Output: 1
print("Stack peek:", stack.peek())  # Output: 1

# Popping the remaining item
print("Popped item:", stack.pop())  # Output: 1

# Trying to pop from an empty stack
print("Popped item:", stack.pop())  # Output: Stack is empty, None
