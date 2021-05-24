# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # interative one pass solution
        # time complexity: o(n + m)
        # space complexity: o(1) constant space
        builder = dummy_head = ListNode(-1)
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                builder.next = l1
                l1 = l1.next
            else:
                builder.next = l2
                l2 = l2.next 
            builder = builder.next
        if l1 == None: builder.next = l2
        if l2 == None: builder.next = l1
        return dummy_head.next
        
