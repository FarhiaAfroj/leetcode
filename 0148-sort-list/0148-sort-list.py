# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        dummy = ListNode(0)
        dummy.next = head
        step = 1
        
        while step < length:
            current = dummy.next
            tail = dummy
            
            while current:
                left = current
                right = self.split(left, step)
                current = self.split(right, step)
                tail = self.merge(left, right, tail)
            step *= 2
        
        return dummy.next
    
    def split(self, head, n):
        
        for i in range(1, n):
            if head:
                head = head.next
            else:
                break
        if not head:
            return None
        next_head = head.next
        head.next = None
        return next_head
    
    def merge(self, l1, l2, tail):
       
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        while tail.next:
            tail = tail.next
        return tail