/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private Integer prev;
    public boolean isValidBST(TreeNode root) {
        // recursive with range as parameters
        // time complexity: o(n)
        // space complexity: o(n)
        // return validate(root, null, null);
        
        // In-order traversal
        prev = null; 
        return inorder(root);
    }
    
    private boolean inorder(TreeNode cur){
        if (cur == null) return true;
        if (!inorder(cur.left)) return false;
        if (prev != null && cur.val <= prev) return false;
        prev = cur.val;
        return inorder(cur.right);
    }
    
    public boolean validate(TreeNode cur, Integer low, Integer high){
        // Empty trees are valid BSTs
        if (cur == null) return true;
        
        // The current node's value must be between low and high
        if ((low != null && cur.val <= low) || 
            (high != null && cur.val >= high)) return false;
        
        // if both left and right are valid
        return validate(cur.left, low, cur.val) && validate(cur.right, cur.val, high);
    }
}
