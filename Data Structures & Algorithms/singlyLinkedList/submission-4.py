class LinkedList:
    
    def __init__(self):
        self.val = None
        self.next = None
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        counter = 0
        current = self.head
        print(self.getValues())
        while current and index >= counter:
            if counter == index:
                return current.val
            current = current.next
            counter += 1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = LinkedList()
        newNode.val = val
        if self.head:
            newNode.next = self.head
        else:
            self.tail = newNode
        self.head = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = LinkedList()
        newNode.val = val
        if self.tail:
            self.tail.next = newNode
        else:
            self.head = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        counter = 0
        current = self.head
        if index == 0:
            if self.head:
                self.head = self.head.next
                return True
            else:
                return False
        while current.next and counter < index:
            if counter == index - 1:
                if self.tail == current.next:
                    self.tail = current
                current.next = current.next.next
                return True
            current = current.next
            counter += 1
        return False

    def getValues(self) -> List[int]:
        current = self.head
        intList = []
        while current:
            intList.append(current.val)
            current = current.next
        return intList
