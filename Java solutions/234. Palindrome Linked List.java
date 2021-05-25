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
    public boolean isPalindrome(ListNode head) {
        /*
            use a extra List 
            time complexity: o(n) 
            space complexity: o(n) for using arraylist
        */ 
        // convert linked list to arraylist
        // List<Integer> vals = new ArrayList<>();
        // ListNode cur = head;
        // while(cur != null){
        //     vals.add(cur.val);
        //     cur = cur.next;
        // }
        // // System.out.println(vals.toString()); // debug print
        // // use two pointer to check for palindrome
        // int front = 0;
        // int back = vals.size() - 1;
        // while (front < back){
        //     if (!vals.get(front).equals(vals.get(back))) return false;
        //     front++;
        //     back--;
        // }
        // return true;
        
        /*  
            in place comparision by reverse the second half
            time complexity: o(4n) -> o(n)
            space complexity: o(1)  
        */
        // find the end of the first half and reverse the second half
        ListNode firstHalfEnd = find_end_of_first_half(head);
        ListNode secondHalfStart = reverse_linked_list(firstHalfEnd.next);
        // compare the first half with the second half
        ListNode p1 = head;
        ListNode p2 = secondHalfStart;
        boolean result = true;
        while (result && p2 != null){
            if (p2.val != p1.val) result = false;
            p1 = p1.next;
            p2 = p2.next;
        }
        // reverse back the second half
        firstHalfEnd.next = reverse_linked_list(secondHalfStart);
        return result;
    }
    
    private ListNode find_end_of_first_half(ListNode head){
        ListNode fast = head;
        ListNode slow = head;
        while(fast.next != null && fast.next.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }
    
    private ListNode reverse_linked_list(ListNode head){
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null){
            ListNode temp_next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp_next;
        }
        return prev;
    }
}
