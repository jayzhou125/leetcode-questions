# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # recursive 
        # time complexity: o(n)
        # space complexity: o(n)
        # def is_mirror(t1, t2):
        #     if t1 == None and t2 == None: return True
        #     if t1 == None or t2 == None: return False
        #     return t1.val == t2.val \
        #            and is_mirror(t1.left, t2.right) \
        #            and is_mirror(t1.right, t2.left)
        # return is_mirror(root, root)
        
        # iterative BFS
        # time complexity: o(n)
        # space complexity: o(n)
        q = []
        q.append(root)
        q.append(root)
        while len(q) != 0:
            t1 = q.pop(0)
            t2 = q.pop(0)
            if t1 == None and t2 == None: continue
            if t1 == None or t2 == None: return False
            if t1.val != t2.val: return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True
