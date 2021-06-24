class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1 # 포인터에 익숙해지니까 매우 유용한듯
        maxgain = 0 # 최소 이득은 0

        for _ in range(len(prices)-1):
            # 현재보다 다음 시점의 가격이 높다면
            if prices[left] <= prices[right]:
                # 그리고 그 차액이 maxgain 보다 크다면
                if maxgain < (prices[right]- prices[left]):
                    # maxgain을 그 차액으로 바꿔준다.
                    maxgain = prices[right]- prices[left]
                    # 그 다음 시점으로 이동한다.
                    right += 1
                # 차액이 maxgain 보다 작다면 일단 다음 시점으로만 이동한다.
                else:
                    right += 1
            # 현재보다 다음 시점 가격이 낮다면
            elif prices[left] > prices[right]:
                # 다음 시점으로 이동한다.
                left = right
                right = left+1

        return maxgain
