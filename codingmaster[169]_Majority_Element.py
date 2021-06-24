from types import *
from typing import List

'''문제
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
# 내 풀이 212 ms
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter

        _dict = Counter(nums)

        return max(_dict, key=(lambda x : _dict[x]))

sol = Solution()
sol.majorityElement([6,5,5])

'''다이나믹 프로그래밍 336 ms
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            # counts에 key로 num이 없으면
            # 추가하고 value로 nums에서 num이 나오는 횟수를 저장.
            if counts[num] == 0:
                counts[num] = nums.count(num)

            # nums에서 num이 과반수를 차지하면
            # 그 수를 바로 반환한다.
            if counts[num] > len(nums) // 2:
                return num
'''
''' 분할정복 Runtime error
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = majorityElement(nums[:half])
        b = majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]
'''

'''다른 풀이
# 156 ms
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return int(median(nums))

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max(counter, key=counter.get)
'''
