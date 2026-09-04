# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        half = length//2

        point = head
        for i in range(half-1):
            point = point.next
        
        second_half = self.reverseList(point.next)

        first = head
        second = second_half

        for i in range(length // 2):
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
        
        if first:
            first.next = None
            
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head = prev

        return head