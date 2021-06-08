# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # recursive
        # time complexity: o(n)
        # space complexity: o(n
        # levels = [] 
        # if root == None: return levels        
        # def helper(node, level):
        #     if len(levels) == level: levels.append([])
        #     levels[level].append(node.val)
        #     if node.left != None: helper(node.left, level + 1)
        #     if node.right != None: helper(node.right, level + 1)    
        # helper(root, 0)
        # return levels
        
        # iterative using list as a queue
        # levels = []
        # if root is None: return levels
        # q = []
        # q.append(root)
        # while len(q) > 0:
        #     level = []
        #     size = len(q)
        #     while size > 0:
        #         node = q.pop(0)
        #         level.append(node.val)
        #         if node.left != None: q.append(node.left)
        #         if node.right != None: q.append(node.right)
        #         size -= 1
        #     levels.append(level)
        # return levels
        
        # iterative optimization with deque()
        from collections import deque
        levels = []
        if root is None: return levels
        q = deque()
        q.append(root)
        while len(q) > 0:
            level = []
            size = len(q)
            while size > 0:
                node = q.popleft()
                level.append(node.val)
                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)
                size -= 1
            levels.append(level)
        return levels
                
        
