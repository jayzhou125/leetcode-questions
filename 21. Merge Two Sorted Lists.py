# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # maintain an unchanging reference to node ahead of the return node.
        dummyHead = builder = ListNode(-1)

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                builder.next = l1
                l1 = l1.next
            else:
                builder.next = l2
                l2 = l2.next
            builder = builder.next
        
        if l1 is None:
            builder.next = l2
        else:
            builder.next = l1
            
        return dummyHead.next
