# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tuple_list = []
        n = head
        while 1:
            # None type error 를 방지하기 위해...
            try:
                v = n.val
                n = n.next
                # 하나하나 뽑아서 현재 node의 value와
                # 다음 node의 value를 리스트에 담는다.
                tuple_list.append((v,n.val))
            except:
                break
        # 리스트의 양 끝에서 하나씩 가져와서 비교한다.
        # 이때 왼쪽에서는 튜플의 첫 번째 값을,
        # 오른쪽에서는 튜플의 두 번째 값을 비교한다.
        for i,v in enumerate(tuple_list[::-1]):
            if tuple_list[i][0] != v[1]:
                return False
        return True
