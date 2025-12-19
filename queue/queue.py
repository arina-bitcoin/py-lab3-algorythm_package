from stack.stack import Node

class Queue:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def enqueue(self, item: int) -> None:
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if self.tail is None:
                raise ValueError("Queue is empty")
            self.tail.next = node
            self.tail = node

        self.size += 1

    def dequeue(self) -> int:
        if self.head is None:
            raise ValueError("Queue is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return value

    def front(self) -> int:
        if self.head is None:
            raise ValueError("Queue is empty")
        return self.head.value

    def is_empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self.size


