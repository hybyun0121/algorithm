# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return list(set(nums1) & set(nums2))


import bisect
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums2.sort()
        for n1 in nums1:
            # 이진검색으로 일치 여부 판별
            # n1이 nums2에 정렬 상태를 유지하고 들어갈 index 반환
            i2 = bisect.bisect_left(nums2, n1)

            [1,2] 2 i2 = 1
                              # 큰 놈 걸러지고            작은 놈 걸러지고
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)
        return result

'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1.intersection(nums2))
'''
