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
    public ListNode reverseList(ListNode head) {        
        // recursive 
        // time complexity: o(n) for n node
        // space complexity: o(n) call stack space
        // if (head == null || head.next == null) return head;
        // ListNode p = reverseList(head.next);
        // head.next.next = head;
        // head.next = null;
        // return p;
        
        /**        
        iterative one pass
        time complexity: o(n)
        space complexity: o(1)
        
        think the algorithm as change the pointing direction, 
        that way it will be easier to understand
        eg. null -> 1 -> 2 -> 3 -> null 
            null <- 1 -> 2 -> 3 -> null
            null <- 1 <- 2 -> 3 -> null
            null <- 1 <- 2 <- 3 -> null
            null <- 1 <- 2 <- 3 <- null
        */
        ListNode prev = null;
        ListNode curr = head;
        while(curr != null){
            ListNode next = curr.next;  // save the next node
            curr.next = prev;           // change the pointing direction
            prev = curr;                // update prev
            curr = next;                // move on to the next node
        }
        return prev;
    }
}
