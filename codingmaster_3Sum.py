from typing import *
def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums)-2):
        #중복 제거
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        #간격을 좁혀가며 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
            # sum = 0인 경우다 정답으로 처리하고 스킵
                results.append((nums[i], nums[left], nums[right]))
                # 이 부분이 왜 필요한거지...
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return results

threeSum([-4, -1, -1, 0, 1, 2])
