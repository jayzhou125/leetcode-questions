# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # one pass use dummy node
        # time complexity: o(n)
        # space complexity: o(1)
        # dummy = ListNode(0)
        # dummy.next = head
        # fast = slow = dummy
        # for _ in range(n):
        #     fast = fast.next
        # while fast.next != None:
        #     fast = fast.next
        #     slow = slow.next
        # slow.next = slow.next.next
        # return dummy.next
        
        # one pass without using dummy node
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
