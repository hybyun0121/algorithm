class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 문자열의 시작지점과 끝지점의 인덱스 번호를 저장한다.
        left, right = 0, len(s)-1

        # 시작지점에서 오른쪽으로, 끝지점에서 왼쪽으로 차례대로 접근하면서
        # 문자를 맞교환 한다.
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1 # 오른쪽으로 한칸 이동
            right -= 1 # 왼쪽으로 한칸 이동
