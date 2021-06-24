class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        root = TrieNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
#############################################################################
'''
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp = self.trie
        word += '#'
        for w in word:
            if w not in tmp:
                tmp[w] = {}
            tmp = tmp[w]


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp = self.trie
        for w in word:
            if w not in tmp:
                return False
            tmp = tmp[w]
        return True if '#' in tmp else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self.trie
        for w in prefix:
            if w not in tmp:
                return False
            tmp = tmp[w]
        return True
-------------------------------------------------------------------------------
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ws = set() # 중복입력 방지
        self.ws_sort = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if word not in self.ws:
            self.ws.add(word)
            # 오름차순으로 정렬된 시퀀스에 word 삽입
            insort(self.ws_sort, word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.ws

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        idx = bisect_left(self.ws_sort, prefix)
        if idx == len(self.ws_sort):
            return False
        return self.ws_sort[idx][:len(prefix)] == prefix
'''
import bisect
a = [1,2,3,4,5]
idx = bisect.bisect_left(a,10)
idx

import insort
ws = set()
ws_sort = []
word = "appzzz"
if word not in ws:
    ws.add(word)
    bisect.insort(ws_sort, word)

ws
ws_sort

_set = set([4,5,23,1,0,0.4,-4])
_set

_set
