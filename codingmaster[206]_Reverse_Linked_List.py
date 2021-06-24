# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rev = None
        node = head
        while node and node.next:
            rev, rev.next, node = node, rev, node.next
        if node:
            rev, rev.next = node, rev

        return rev
