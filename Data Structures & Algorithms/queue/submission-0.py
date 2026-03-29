class Deque:
    
    def __init__(self):
        self.val = None
        self.next = None
        self.prev = None
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if self.head and self.tail:
            return False
        return True

    def append(self, value: int) -> None:
        newNode = Deque()
        newNode.val = value
        if self.isEmpty():
            self.head = self.tail = self.val = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def appendleft(self, value: int) -> None:
        newNode = Deque()
        newNode.val = value
        if self.isEmpty():
            self.head = self.tail = self.val = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_value = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        return last_value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_value = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return first_value
