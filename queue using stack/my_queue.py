class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s = str(current.item) + ' ' +s
            current = current.next
        return 'bottom -> '+ s+'<- top'

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
