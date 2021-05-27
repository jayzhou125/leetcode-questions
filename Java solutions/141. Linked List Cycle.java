/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        // hash set, slow run time
        // time complexity: o(n)
        // space complexity: o(n)
        // Set<ListNode> visited = new HashSet<>();
        // while (head != null){
        //     if (visited.contains(head)) return true;
        //     visited.add(head);
        //     head = head.next;
        // }
        // return false;
        
        // no extra space
        // time complexity: o(n + m) n is the number of nodes in the list, 
        //                           m is the number of nodes in the cycle
        // space complexity: o(1)
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }
}
