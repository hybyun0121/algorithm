'''문제
Given a string expression of numbers and operators,
return all possible results from computing all the different
possible ways to group numbers and operators. You may return
the answer in any order.
'''

# 책 풀이 88ms
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []

            # eval은 string으로 들어온 숫자 계산을 수행해주는 메소드이다.
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))

            return results

        # 숫자 뿐이면 리스트에 int type으로 담아서 반환
        if expression.isdigit():
            return [int(expression)]

        results = []
        for index, value in enumerate(expression):
            if value in "-+*":
                # expression을 하나하나 가져와서 연산자 이면
                # 양쪽으로 나누어 재귀적으로 처리
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])

                results.extend(compute(left, right, value))
        return results
        
'''다른풀이 16ms
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if len(expression) < 2:
            return [int(expression)]
        ans = []
        m = {}
        op = {
            '*': lambda x, y: x * y,
            '-': lambda x, y: x - y,
            '+': lambda x, y: x + y,
        }

        def divideandconquer(s):
            if s in m:
                return m[s]
            left, right, res = [], [], []
            for i in range(len(s)):
                if s[i] in op:
                    s1 = s[0:i]
                    s2 = s[i + 1:]
                    left = divideandconquer(s1)
                    right = divideandconquer(s2)
                    for l in m[s1]:
                        for r in m[s2]:
                            res.append(op[s[i]](l,r))
            if not res:
                res.append(int(s))
            m[s] = res
            return res

        ans = divideandconquer(expression)
        return ans
'''
