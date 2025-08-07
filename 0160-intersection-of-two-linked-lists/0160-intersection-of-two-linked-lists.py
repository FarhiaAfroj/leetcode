# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        Returns the node where the two singly linked lists intersect,
        or None if they do not intersect.
        """
        a = headA
        b = headB
        while a is not b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a  # Intersection node or None

