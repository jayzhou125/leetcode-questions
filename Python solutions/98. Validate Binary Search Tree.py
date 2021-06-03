# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    def isValidBST(self, root: TreeNode) -> bool:
        # recursive with range of low and high
        # time complexity: o(n)
        # space complexity: o(n)
        # def validate(cur, low, high):
        #     if cur == None: return True
        #     if (low != None and cur.val <= low) or \
        #        (high != None and cur.val >= high): return False
        #     return validate(cur.left, low, cur.val) and validate(cur.right, cur.val, high)
        # return validate(root, None, None)
        
        # inorder traversal
        global prev
        prev = None
        def inorder(cur):
            global prev
            if cur == None: return True
            if not inorder(cur.left): return False
            if prev != None and cur.val <= prev: return False
            prev = cur.val
            return inorder(cur.right)
        return inorder(root)
