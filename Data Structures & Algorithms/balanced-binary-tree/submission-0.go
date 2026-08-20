/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func abs(val1 int, val2 int) int {
    res := val1 - val2
    fmt.Println("Res",res)
    if res >= 0 {
        return res
    }

    return -res
}

func dfs(node *TreeNode) int {
    if node == nil{
        return 0
    }

    left := dfs(node.Left)

    if left == -1 {
        return -1
    }

    right := dfs(node.Right)
    if right == -1 {
        return -1
    }

    if abs(left,right) > 1{
        return -1
    }

    return max(left, right) + 1
}

func isBalanced(root *TreeNode) bool {
    // Invariant: Absolute difference between left and right must be less than equal to 1
    // State: Left and right height
    // Violate: Abs diff of left and right more than 1
    // Recover: If more than 1 return -1 (if -1 then it is not height-balanced)

    if root == nil{
        return true
    }

    return dfs(root) != -1
    
}
