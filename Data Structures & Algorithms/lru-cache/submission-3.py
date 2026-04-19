class LRUCache:
    from collections import deque
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.recentlyUsed = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            self._resetCachePosition(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self._resetCachePosition(key)

    def _resetCachePosition(self, key) -> None:
        if key in self.recentlyUsed:
            self.recentlyUsed.remove(key)
        self.recentlyUsed.appendleft(key)
        if len(self.recentlyUsed) > self.capacity:
            remove = self.recentlyUsed.pop()
            self.cache.pop(remove, None)
