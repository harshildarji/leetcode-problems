# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = f = head
        while s and f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False
