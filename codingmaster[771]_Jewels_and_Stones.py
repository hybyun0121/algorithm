class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        _dic = {}
        for s in stones:
            if s not in _dic:
                _dic[s] = 1
            else:
                _dic[s] += 1
        total = 0
        for s in jewels:
            if s in _dic:
                total += _dic[s]

        return total

from collections import OrderedDict, defaultdict

a = defaultdict(list)
a[0]
