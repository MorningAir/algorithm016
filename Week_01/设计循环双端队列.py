class MyCircularDeque:

    def __init__(self, k: int):
        self.head,self.tail = 0,0
        self.capacity = k+1
        self.arr = [0 for _ in range(k+1)]


    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.head = (self.head+self.capacity-1)%self.capacity
            self.arr[self.head] = value
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.arr[self.tail] = value
            self.tail = (self.tail+1)%self.capacity
            return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.head = (self.head+1)%self.capacity
            return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.tail = (self.tail+self.capacity-1)%self.capacity
            return True


    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.arr[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.arr[(self.tail-1+self.capacity)%self.capacity]

    def isEmpty(self) -> bool:
        return self.head==self.tail
    def isFull(self) -> bool:
        return (self.tail+1)%self.capacity == self.head