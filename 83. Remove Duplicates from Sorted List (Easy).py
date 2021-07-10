# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        result = current = ListNode(0)
        while head.next:
            if head.val != head.next.val:
                current.next = head
                current = current.next
            head = head.next
        current.next = head
        return result.next

        