class minHeap :
    def __init__(self, capacity) :
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0
    def getParentIndex(self, index) :
        return (index - 1) // 2
    def getLeftChildIndex(self, index) :
        return (2 * index) + 1
    def getRightChildIndex(self, index) :
        return (2 * index) + 2
    def hasParent(self, index) :
        return self.getParentIndex(index) >= 0
    def hasLeftChild(self, index) :
        return self.getLeftChildIndex(index) < self.size
    def hasRightChild(self, index) :
        return self.getRightChildIndex(index) < self.size
    def isFull(self) :
        return self.size == self.capacity
    def swap(self, index1, index2) :
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]
    def insert(self, data) :
        if self.isFull() :
            raise("Heap is Full")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1)
    def heapifyUp(self, index) :
        if (self.hasParent(index) and self.storage[self.getParentIndex(index)] > self.storage[index]) :
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))
    def print(self) :
        for i in range(self.size) :
            print(self.storage[i], end = " ")
    def removeMin(self) :
        if self.size == 0 :
            raise("Empty Heap")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return data
    def heapifyDown(self) :
        index = 0
        while self.hasLeftChild(index) :
            smallerIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.storage[(self.getRightChildIndex(index))] < self.storage[smallerIndex] :
                smallerIndex = self.getRightChildIndex(index)
            if self.storage[index] < self.storage[smallerIndex] :
                break
            else :
                self.swap(index, smallerIndex)
            index = smallerIndex
        
mm = minHeap(10)
mm.insert(15)
mm.insert(14)
mm.insert(13)
mm.insert(12)
mm.insert(11)
mm.insert(10)
mm.insert(9)


print(mm.removeMin())
print(mm.removeMin())
print(mm.removeMin())









