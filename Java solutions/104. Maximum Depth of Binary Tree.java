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
    public int maxDepth(TreeNode root) {
        // recursion
        // time complexity: o(n) 
        // space complexity: the height of the tree, 
        //                   worst case o(n), unbalanced, like a linked list
        //                   best case o(log(n)), completedly balanced binary tree
        // if (root == null) return 0;
        // int left_h = maxDepth(root.left);
        // int right_h = maxDepth(root.right);
        // return java.lang.Math.max(left_h, right_h) + 1;
        
        // iterative DFS
        // time complexity: o(n)
        // space complexity: same as using recursion, since we are using stack
        // if (root == null) return 0;
        // Stack<TreeNode> stack = new Stack<>();
        // Stack<Integer> depths = new Stack<>();
        // stack.push(root);
        // depths.push(1);
        // int depth = 0, cur_depth = 0;
        // while(!stack.empty()){
        //     TreeNode cur = stack.pop();
        //     cur_depth = depths.pop();
        //     if (cur != null){
        //         depth = Math.max(depth, cur_depth);
        //         stack.push(cur.right);
        //         depths.push(cur_depth + 1);
        //         stack.push(cur.left);
        //         depths.push(cur_depth + 1);
        //     }
        // }
        // return depth;
        
        // DFS optimization for not push null nodes
        // if (root == null) return 0;
        // Stack<TreeNode> stack = new Stack<>();
        // Stack<Integer> depths = new Stack<>();
        // int max_depth = 1;
        // stack.push(root);
        // depths.push(1);
        // while (!stack.empty()) {
        //     TreeNode cur = stack.pop();
        //     int cur_depth = depths.pop();
        //     if (cur.left == null && cur.right == null) {
        //         max_depth = Math.max(max_depth, cur_depth);
        //     } 
        //     if (cur.right != null) {
        //         stack.push(cur.right);
        //         depths.push(cur_depth + 1);
        //     } 
        //     if (cur.left != null) {
        //         stack.push(cur.left);
        //         depths.push(cur_depth + 1);
        //     }
        // }
        // return max_depth;
        
        // BFS
        // linkedList.offer adds the element to the tail of the list
        // linkedList.poll retrieves and removes the head (first element) of the list
        if (root == null) return 0;
        int max_depth = 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root); // offer() is prefered compare to add(), because offer will throw exception
        while (!q.isEmpty()) {
            int size = q.size();
            max_depth++;
            while (size > 0) {
                TreeNode node = q.poll(); // poll() will return null if queue is empty
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
                size--;
            }
        }
        return max_depth;
    }
}
