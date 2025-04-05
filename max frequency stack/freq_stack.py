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

class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxfreq = 0

    def push(self, val: int) -> None:
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f

        if f > self.maxfreq:
            self.maxfreq = f

        if f not in self.group:
            self.group[f] = MyStack()

        self.group[f].push(val)

    def pop(self) -> int:
        if self.maxfreq == 0:
            raise ValueError("FreqStack is empty.")

        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1

        if self.group[self.maxfreq].empty():
            self.maxfreq -= 1

        return val

