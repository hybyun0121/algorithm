from types import *

class Solution:
    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
        answer = ""
        window = len(t)
        if s == t:
            return t

        while window < len(s)+1:
            i = 0
            while window + i < len(s):
                print("window size:",window)
                if self.check_window(t, s[i:window+i]):
                    return s[i:window+i]
                else:
                    i += 1
            if self.check_window(t, s[-1*window:]):
                return s[-1*window:]
            window += 1
        print("last wind :", window)
        if self.check_window(t, s[-1*window:]):
            return s[-1*window:]
        return answer

    def check_window(self, target: str, win_word: str) -> bool:
        t_C = Counter(list(target))
        w_C = Counter(list(win_word))
        print(w_C)

        for k in t_C.keys():
            if w_C[k] < t_C[k]:
                return False
        return True

sol = Solution()
sol.minWindow(s="aaaaaaaaaaaabbbbbcdd", t="abcdd")
