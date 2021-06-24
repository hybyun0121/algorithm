class MyCircularQueue:

    def __init__(self, k: int):
        self.cq = [None] * k
        self.k = k


    def enQueue(self, value: int) -> bool:
        for i in range(self.k):
            if self.cq[i] == None:
                self.cq[i] = value
                return True
        for j in range(1, len(value)-self.k):
            self.cq[j] = value[j+self.k]
        return False

    def deQueue(self) -> bool:
        if self.cq[0] != None:
            self.cq[0] = None
            return True
        else:
            return False

    def Front(self) -> int:
        if self.cq == [None]*k or self.cq[0] == None:
            return -1
        else:
            return self.cq[0]

    def Rear(self) -> int:
        if self.cq == [None]*self.k or self.cq[-1] == None:
            return -1
        else:
            return self.cq[-1]

    def isEmpty(self) -> bool:
        if self.cq == [None]*k:
            return False
        else:
            return True

    def isFull(self) -> bool:
        if None in self.cq:
            return False
        else:
            True


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
