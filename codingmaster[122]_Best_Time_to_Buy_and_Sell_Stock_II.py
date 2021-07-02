from typing import List

# 내 풀이 52ms
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1, p2 = 0, 1
        cache = 0
        n = len(prices)

        # p2가 배열의 마지막 까지 가면 while문을 종료합니다.
        while p2 < n:
            # p1에서 p2까지 구간의 수익이 양수인 경우
            if (prices[p2] - prices[p1] > 0):
                # p2가 아직 마지막 배열 index는 아니고 p2+1이 더 큰 수익이 될때
                if (p2 < n-1) and (prices[p2] - prices[p2+1]) < 0:
                    p2 += 1 # p2를 한 칸 옮겨 더 큰 수익을 낸다.
                
                # 그게 아니라면 수익 실현을 하고 다음 수익이 날때 까지 기다린다.
                else:
                    cache += prices[p2] - prices[p1]
                    p1 = p2 + 1
                    p2 = p1 + 1
            # 구간 사이 손해를 본다면 포인트를 계속 다음 칸으로 옮기면서
            # 기다린다.
            else:
                p1 = p2
                p2 = p1 + 1
        
        return cache

sol = Solution()
prices = [[7,1,5,3,6,4],
          [1,2,3,4,5],
          [7,6,4,3,1]]
for pr in prices:
    print(sol.maxProfit(pr))

# 다른 풀이 36ms...
# 내 풀이 보다 훨씬 greedy한 듯.
# 훨씬 더 직관적인 단타 느낌
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range (1,len(prices)):
            # 한 칸씩 옮겨가며 수익이 생길때마다
            # profit에 발생한 수익을 더해준다.
            if prices [i] > prices[i-1]:
                profit+= prices[i]-prices[i-1]
        return profit
'''