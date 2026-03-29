class DynamicArray:
    array = []
    size = 0
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if(self.size >= self.getCapacity()):
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]


    def resize(self) -> None:
        resized_array = []
        for i in self.array:
            resized_array.append(i)
        for _ in self.array:
            resized_array.append(0)
        self.array = resized_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.array)