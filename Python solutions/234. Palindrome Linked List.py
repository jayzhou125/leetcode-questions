# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # use extra list
        # time complexity: o(n)
        # space complexity: o(n)
        # cur = head
        # vals = []
        # while cur != None:
        #     vals.append(cur.val)
        #     cur = cur.next
        # front = 0
        # back = len(vals) - 1 
        # while front < back:
        #     if vals[front] != vals[back]: return False
        #     front += 1
        #     back -= 1
        # return True
        
        # use in place comparision by reverse the second half 
        # time complexity: o(n)
        # space complexity: o(1)
        def find_first_half_end(head) -> ListNode:
            fast = slow = head
            while fast.next != None and fast.next.next != None:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def reverse(head) -> ListNode:
            prev, curr = None, head
            while curr != None:
                curr.next, prev, curr = prev, curr, curr.next
            return prev
        
        if head == None or head.next == None: return True
        
        # find the end of first half and reverse the second half
        firstHalfEnd = secondHalfStart = ListNode()
        firstHalfEnd = find_first_half_end(head)
        secondHalfStart = reverse(firstHalfEnd.next)
        
        # compare first half with the second half
        p1, p2, result = head, secondHalfStart, True
        while result and p2 != None:
            if p1.val != p2.val: result = False
            p1 = p1.next
            p2 = p2.next
        
        # reverse the second half back
        firstHalfEnd.next = reverse(secondHalfStart)
        
        return result

        
        
        
        

    
    
