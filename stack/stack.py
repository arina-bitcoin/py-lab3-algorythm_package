class Node:
    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next = next_node

class Stack:
    def __init__(self):
        self.top: Node | None  = None # Вершина основного стека
        self.min_top: Node | None  = None # Вершина стека минимумов
        self.size: int = 0
    
    def push(self, x: int) -> None:
        new_node = Node(x, self.top)
        self.top = new_node
        self.size += 1
        
        if self.min_top is None or x <= self.min_top.value:
            new_min_node = Node(x, self.min_top)
            self.min_top = new_min_node
    
    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        
        if value == self.min_top.value:
            self.min_top = self.min_top.next
            
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
        return self.min_top.value
    


if __name__ == "__main__":
    s = Stack()
  
    s.push(5)
    print(f"После push(5): {s}, min={s.min()}")
    
    s.push(3)
    print(f"После push(3): {s}, min={s.min()}")
    
    s.push(7)
    print(f"После push(7): {s}, min={s.min()}")
    
    s.push(3)
    print(f"После push(3): {s}, min={s.min()}")
    
    print(f"pop() = {s.pop()}")
    print(f"После pop(): {s}, min={s.min()}")
    
    print(f"pop() = {s.pop()}")
    print(f"После pop(): {s}, min={s.min()}")
    
    print(f"Размер стека: {len(s)}")
    print(f"Пустой ли стек: {s.is_empty()}")
    print(f"Верхний элемент: {s.peek()}")