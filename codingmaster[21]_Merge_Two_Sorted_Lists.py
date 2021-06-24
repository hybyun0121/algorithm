# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sor = None
        temp = []
        while l1 and l2:
            temp.append(l1.val)
            temp.append(l2.val)
            l1 = l1.next
            l2 = l2.next
        while l1:
            temp.append(l1.val)
            l1 = l1.next
        while l2:
            temp.append(l2.val)
            l2 = l2.next

        temp = sorted(temp)

        for t in temp[::-1]:
            sor, sor.next = ListNode(t), sor
            sor.next

        return sor
