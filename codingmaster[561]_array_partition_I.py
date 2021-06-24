class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # idea : 두 쌍 중 작은걸 뽑아 더 하기 때문에
        #        최댓값을 구하려면 비슷한거 끼리 묶어야 한다.
        nums.sort() # 그래서 정렬함
        min_sum = 0 # pair 중 작은걸 뽑아 더할 변수 지정
        k = 0 # 인덱스 0 부터 시작

        for _ in range(len(nums)//2):
            min_sum += min(nums[k], nums[k-1])
            k += 2 # 두 개가 한 쌍이니 2칸씩 뛰어간다.
        return min_sum
# 속도가 332ms 나왔다....왜이렇게 느린가...어떻게 하면 빠르게 할 수 있을까?
