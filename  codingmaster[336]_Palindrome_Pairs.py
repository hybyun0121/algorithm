class Solution:
    def is_palin(self, sen):
        return sen == sen[::-1]

    def palindromePairs(self, words):
        _join = []
        for i, w_c in enumerate(words):
            for w in range(len(w_c)+1):
                pre = w_c[:w]
                suf = w_c[w:]
                if self.is_palin(pre) and self.is_palin(suf) and pre in words:
                    if i != words.index(pre):
                        _join.append([i, words.index(pre)])
                elif self.is_palin(suf) and pre[::-1] in words:
                    _join.append([i, words.index(pre[::-1])])

        return _join

words = ["abcd","dcba","lls","s","sssll"]
sol = Solution()
sol.palindromePairs(words)
