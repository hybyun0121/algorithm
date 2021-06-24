class Solution:
    def isPalindrome(self, s: str) -> bool:
        az = []
        # 문자열에서 문자를 하나씩 뽑아서 알파벳이나 숫자이면
        # 소문자로 변환시켜준 뒤 새로운 리스트에 담는다.
        for c in s:
            if c.isalnum():
                az.append(c.lower())
        # 문자와 숫자만 담긴 새리스트를 뒤집어서 다른 변수에 담아준다.
        za = az[::-1]

        # 두 개의 리스트가 같거나 비어있으면 True를 return 한다.
        if az==za or len(az) <= 1:
            return True
        else:
            return False
