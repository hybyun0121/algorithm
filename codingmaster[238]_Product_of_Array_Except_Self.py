class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        temp = []

        for i in range(len(nums)-1):
            # 슬라이싱을 이용해서 해당 인덱스를 뺀 나머지 값들을 두 리스트에 담는다.
            # 해당 인덱스 기준 왼쪽 애들은 left, 오른쪽 애들은 right 리스트에 담아준다.
            left = nums[:3]
            right = nums[i+1:]
            # 다시 하나의 리스트로 만들어 준다.
            prod_list = left+right
            # 곱한 결과를 temp 리스트에 담고 다음 인덱스로 넘어간다.
            temp.append(math.prod(prod_list))
        # 마지막 인덱스는 제일 마지막 원소를 뺀 나머지 아이들의 곱이다.
        temp.append(math.prod(nums[:-1]))

        return temp

# -1,1 폭탄에서 시간초과....
