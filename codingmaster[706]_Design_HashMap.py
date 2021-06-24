# 공간적으로 매우 비효율적...
'''
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.hashmap = [[]] * 500

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.size
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        self.hashmap[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.hashmap[key] = -1
'''

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 500
        self.hashmap = [[]] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.size

        if len(self.hashmap[idx]) == 0:
            self.hashmap[idx] = [[key, value]]
        else:
            hashmap[0][[1,2]]
            (key : 11, value : 20)

            for i, j in enumerate(self.hashmap[idx]):
                if j[0] == 11:
                    self.hashmap[idx][i] = [j[0], value]
                    break
                else:
                    self.hashmap[idx].append([key,value])
                    break

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.size
        try:
            hashmap[0][[]]
            for i, p in enumerate(self.hashmap[idx]):
                if p[0] == 11:
                    return p[1]
        except:
            return -1
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.size
        try:
            for i, p in enumerate(self.hashmap[idx]):
                if p[0] == key:
                    del self.hashmap[idx][i]
        except:
            pass
