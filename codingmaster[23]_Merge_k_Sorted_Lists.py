# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        _list = []
        for list in lists:
            if list:
                while not list.next == None:
                    _list.append(list.val)
                    list = list.next
                _list.append(list.val)
        if not _list:
            return None

        _list = sorted(_list)

        temp = point = ListNode()
        while len(_list)-1:
            point.val = _list.pop(0)
            point.next = ListNode()
            point = point.next

        point.val = _list[-1]

        return temp
