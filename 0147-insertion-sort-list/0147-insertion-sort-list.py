# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)   
        current = head
        
        while current:
            prev = dummy
            next_node = current.next
           
            while prev.next and prev.next.val < current.val:
                prev = prev.next
           
            current.next = prev.next
            prev.next = current
            current = next_node
        
        return dummy.next