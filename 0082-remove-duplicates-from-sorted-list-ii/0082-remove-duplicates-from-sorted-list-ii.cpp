
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr) return head;
        
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;
        ListNode* curr = head;
        
        while (curr != nullptr) {
            bool isDuplicate = false;
            while (curr->next != nullptr && curr->val == curr->next->val) {
                isDuplicate = true;
                curr = curr->next;
            }
            if (isDuplicate) {
                prev->next = curr->next;
            } else {
                prev = curr;
            }
            curr = curr->next;
        }
        
        return dummy->next;
    }
};