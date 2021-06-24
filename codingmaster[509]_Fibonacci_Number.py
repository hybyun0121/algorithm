'''Brute force(820ms)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

sol = Solution()
sol.fib(n=3)
'''

'''Memoization(44ms)
class Solution:
    import collections
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]
        dp[n] = self.fib(n-1) + self.fib(n-2)
        return dp[n]
'''
'''Tabulation
class Solution:
    import collections
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        self.dp[1] = 1

        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[n]
'''
'''Space complexity(O(1))(40ms)
x = 0, y = 1
0+1 = 1
  1 + 1 = 2
      1 + 2 = 3
           ...
--------------------------
X +   Y   = C
    X_new + Y_new = C_new
                 ....
--------------------------
def Solution:
    def fib(self, n: int) -> int:
        x=0, y=1
        for _ in range(0, n):
            x,y = y, x+y
        return x
'''
