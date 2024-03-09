class Stack01:
    def __init__(self):
        self.items=[]
        
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
    
my_stack = Stack01()
my_stack.push(1)
my_stack.push(2)
print(my_stack.items)
print(my_stack.pop())
print(my_stack.items)
        