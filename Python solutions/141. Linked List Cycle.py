# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # hashset
        # time complexity: o(n)
        # space complexity: o(n)
        # visited = set()
        # while head != None:
        #     if head in visited: return True
        #     visited.add(head)
        #     head = head.next
        # return False
    
        # no extra space, also known as Floyd's Cycle Finding Algorithm
        # time complexity: o(n(# of nodes in list) + m(# of nodes in cycle)) -> o(n)
        # space complexity: o(1)
        fast = slow = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False
        
