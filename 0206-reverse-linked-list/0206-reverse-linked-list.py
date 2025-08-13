class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur:
            nxt = cur.next         # save next node
            cur.next = prev        # reverse pointer
            prev = cur             # move prev forward
            cur = nxt              # move cur forward
        return prev                # prev becomes new head
