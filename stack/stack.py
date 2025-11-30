class Node:
    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next = next_node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self.min_stack = []
    
    def push(self, x: int) -> None:
        new_node = Node(x, self.top)
        self.top = new_node
        self.size += 1
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value
    
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.value
    
    def is_empty(self) -> bool:
        return self.top is None
    
    def __len__(self) -> int:
        return self.size
    
    def min(self) -> int:
        if self.is_empty():
            raise IndexError("Min from empty stack")
        return self.min_stack[-1]