class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 예외처리 4ms 당겨줌
        if not nums:
            return -1

        left, right = 0, len(nums) -1
        while left < right:
            mid = left + (right-left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # pivot = nums.index(min(nums)) # 시간 오래 걸릴 듯
        pivot = left
        # pivot = mid # case [1],0 에서 걸림

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] == target:
                return mid_pivot
            elif nums[mid_pivot] > target:
                right = mid-1
            elif nums[mid_pivot] < target:
                left = mid + 1
        return -1

''' 내가 짠거랑 별 차이 안남 예외처리 빼면 런타임은 똑같음
class Solution:
    def search_index(self, nums, target):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        # 길이가 1인 리스트는 바로 서치
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        # 정렬한 리스트를 따로 담아준다.
        sorted_nums = sorted(nums)

        # 정렬한게 원래 리스트와 같다면 여기서 바로 서치
        if sorted_nums == nums:
            return self.search_index(nums, target)

        # 순서가 바뀌기 전 0번째 수의 nums에서 index를 저장.
        start_idx = (len(nums)-1) - self.search_index(sorted_nums, nums[0]) + 1

        # start_idx를 기준으로 둘로 나누었을때 target이 앞쪽 범위에 속하는지 아닌지를 알아내고
        # 해당하는 범위만큼 슬라이싱 해서 서치 없으면 0
        if (target >= nums[0]) and (target <= nums[start_idx-1]):
            print(nums[:start_idx])
            if self.search_index(nums[:start_idx], target) == -1:
                return -1
            return self.search_index(nums[:start_idx], target)

        elif (target <= nums[-1]) and (target >= nums[start_idx]):
            print(nums[start_idx:])

            if self.search_index(nums[start_idx:], target) == -1:
                return -1
            return self.search_index(nums[start_idx:], target) + start_idx
        else:
            return -1
'''
