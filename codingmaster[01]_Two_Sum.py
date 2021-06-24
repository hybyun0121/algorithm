class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums) # 정렬 때리기
        left, right = 0, len(sorted_nums)-1 # 포인트(?)를 이용하기

        # 무한루프에 빠질까 쫄지 말자
        while True:
            # 더 해서 타겟 값이면, nums 에서 해당하는 값의 리스트를 return
            if target == (sorted_nums[right] + sorted_nums[left]):
                num1 = nums.index(sorted_nums[left])
                nums[num1] = 'z'   # [3,3] 이런 녀석은 계속 앞에 인덱스가 나오니까...
                return [num1, nums.index(sorted_nums[right])]
            # 더 했는데 타겟보다 크니까 오름 정렬된 리스트에서 오른쪽 포인트를 왼쪽으로 한 칸 옮겨
            elif target < (sorted_nums[right] + sorted_nums[left]):
                right -= 1
            # 더 했는데 타겟보다 작으니까 오름 정렬된 리스트에서 왼쪽 포인트를 오른으로 한 칸 옮겨
            elif target > (sorted_nums[right] + sorted_nums[left]):
                left += 1
            # 무한루프에 빠질까봐 살짝 쫄아서...
            else:
                print("ERROR")
                break

# Solution 01 - Brute-Force
def twoSum_sol1(nums, target):
    # [1,2,3,4,5]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

# Solution 02 - in 이용한 탐색
def twoSum_sol2(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        # target에서 뺀 나머지가 뒤에 있을까??
        if complement in nums[i+1:]:
            # list.index(v) : value 가 위치한 인덱스 반환
            return nums.index(n), nums[i+1:].index(complement) + (i+1)

for i, v in enumerate(a):
    print(i,v)


3 in a
-1 in a
