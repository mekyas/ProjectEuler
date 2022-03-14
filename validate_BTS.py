class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, max_val, min_val):
            if root is None:
                return True
            if root.left is not None:
                if root.left.val >= min_val:
                    return False
            if root.right is not None:
                if root.right.val <= max_val:
                    return False
            left = helper(root.left, max_val, min(min_val, root.val))
            right = helper(root.right, max(max_val, root.val), min_val)
            return left and right
        return helper(root, root.val, root.val)

s = Solution()
root = TreeNode(val=5, left=TreeNode(val=1), right=TreeNode(val=4, left=TreeNode(val=3), right=TreeNode(val=6)))
print(s.isValidBST(root))