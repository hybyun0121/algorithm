class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.cir_deque = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        temp = self.cir_deque[::-1]
        if 1 <= len(self.cir_deque) < self.k:
            temp.append(value)
            self.cir_deque = temp[::-1]
            return True
        elif len(self.cir_deque) == self.k:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if 1 <= len(self.cir_deque) < self.k:
            self.cir_deque.append(value)
            return True
        elif len(self.cir_deque) == self.k:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not len(self.cir_deque) == 0:
            temp = self.cir_deque[::-1]
            del temp[0]
            self.cir_deque = temp[::-1]
            return True
        elif len(self.cir_deque) == 0:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not len(self.cir_deque) == 0:
            del self.cir_deque[-1]
            return True
        elif len(self.cir_deque) == 0:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.cir_deque[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return None
        return self.cir_deque[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if len(self.cir_deque) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if len(self.cir_deque) == self.k:
            return True
        else:
            return False
