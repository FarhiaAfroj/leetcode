# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
       
        less_head = ListNode(0)
        greater_equal_head = ListNode(0)
        less_ptr = less_head
        greater_equal_ptr = greater_equal_head
        
        current = head
        while current:
            if current.val < x:
                less_ptr.next = current
                less_ptr = less_ptr.next
            else:
                greater_equal_ptr.next = current
                greater_equal_ptr = greater_equal_ptr.next
            current = current.next
        
       
        less_ptr.next = greater_equal_head.next
        greater_equal_ptr.next = None
        
        return less_head.next