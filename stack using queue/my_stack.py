class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        if self.head is None:
            self.tail = Node(x)
            self.head = self.tail
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next

    def pop(self) -> int:
        if self.head:
            item = self.head.item
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')
        
    def peek(self) -> int:
        return self.head.item

    def empty(self) -> bool:
        return self.head is None

class MyStack:

    def __init__(self):
        self.q = MyQueue()
        self.size = 0

    def push(self, x: int) -> None:
        self.q.push(x)
        self.size += 1
        for _ in range(self.size - 1):
            self.q.push(self.q.pop())

    def pop(self) -> int:
        if self.empty():
            raise ValueError("Stack is empty.")
        self.size -= 1
        return self.q.pop()

    def top(self) -> int:
        if self.empty():
            raise ValueError("Stack is empty.")
        return self.q.peek()

    def empty(self) -> bool:
        return self.size == 0
