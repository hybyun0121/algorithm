from typing import *
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    total = nums1 + nums2).sort()
    if len(total) % 2 == 0:
        mid1 = total[(len(total)-1) // 2]
        mid2 = total[((len(total)-1) // 2) + 1]
        return (mid1+mid2) / 2
    else:
        return total[(len(total)-1) // 2]

nums1 = [0,0,0,0,0]
nums2 = [-1,0,0,0,0,0,1]
total = list(set(nums1 + nums2)).sort()
total
total.sort()
type(total)
