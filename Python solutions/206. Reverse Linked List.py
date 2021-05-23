# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recursive 
        # time complexity: o(n)
        # space complexity: o(n) for call stack
        # if head == None or head.next == None: return head
        # new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head
        
        # iterative one pass
        # time complexity: o(n)
        # space complexity: o(1)
        # prev = None
        # curr = head
        # while curr != None:
        #     temp_next = curr.next   # save the next node
        #     curr.next = prev        # change the pointing direction
        #     prev = curr             # update prev
        #     curr = temp_next        # move on to the next node
        # return prev
        
        # use python Swap, easier to write and remember
        pre, cur = None, head
        while cur != None:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
    
