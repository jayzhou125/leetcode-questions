/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // one pass iterative
        // time complexity: o(n + m) 
        // space complexityL: o(1)
        ListNode dummy_head = new ListNode(-1);
        ListNode builder = dummy_head;
        while (l1 != null && l2 != null){
            if (l1.val <= l2.val){
                builder.next = l1;
                l1 = l1.next;
            } else {
                builder.next = l2;
                l2 = l2.next; 
            }
            builder = builder.next; 
        }
        // if we are at this point, that means 
        // either l1 or l2 still have some nodes left
        // we need to append the rest
        builder.next = l1 == null ? l2 : l1; 
        return dummy_head.next;
    }
}
