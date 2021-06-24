# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        rev_start = ListNode(None)
        rev_start.next = head
        for _ in range(m-1):
            rev_start = rev_start.next

        curr_node = rev_start.next
        next_node = curr_node.next
        for _ in range(n-m):
            curr_node.next, next_node.next, rev_start, rev_start.next =\
             next_node.next, rev_start.next, next_node


        print(rev_start)
        print(curr_node)
        print(next_node)

        return head
