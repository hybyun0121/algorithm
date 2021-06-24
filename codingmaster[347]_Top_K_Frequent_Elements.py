class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sordict = {}
        for n in nums:
            if n not in sordict.keys():
                sordict[n] = 1
            else:
                sordict[n] += 1

        sordict = dict(sorted(sordict.items(), key=lambda x: x[1], reverse=True))

        return list(sordict.keys())[:k]
