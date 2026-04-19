class Node:
    def __init__(self, key: int, value:int):
        self.key, self.value = key, value
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = self.right = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
        
        if len(self.cache.keys()) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]
    
    def _remove(self, node) -> None:
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def _insert(self, node) -> Nonde:
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        node.prev = prev
        self.right.prev = node