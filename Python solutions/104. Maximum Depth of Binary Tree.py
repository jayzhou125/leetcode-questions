# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # recursive
        # time complexity: o(n)
        # space complexity: o(n) worst case, o(logn) best case
        # if root == None: return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
        # DFS iterative
        # if root == None: return 0
        # stack = []
        # depths = []
        # max_depth = 1
        # stack.append(root)
        # depths.append(1)
        # while len(stack) != 0:
        #     cur = stack.pop()
        #     cur_depth = depths.pop()
        #     if cur.left == None and cur.right == None:
        #         max_depth = max(cur_depth, max_depth)
        #     if cur.left != None: 
        #         stack.append(cur.left)
        #         depths.append(cur_depth + 1)
        #     if cur.right != None: 
        #         stack.append(cur.right)
        #         depths.append(cur_depth + 1)
        # return max_depth
        
        # BFS iterative
        from collections import deque
        if root == None: return 0
        q = deque()
        max_depth = 0
        q.append(root)
        while len(q) != 0:
            size = len(q)
            max_depth += 1
            while size > 0:
                cur = q.popleft()
                if cur.left != None: q.append(cur.left)
                if cur.right != None: q.append(cur.right)
                size -= 1
        return max_depth
                
             
