# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = current = ListNode(0)
        value = 0
        while l1 or l2 or value:
            value += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current.next = current = ListNode(value % 10)
            value //= 10
        return result.next