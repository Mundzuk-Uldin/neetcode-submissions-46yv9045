# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self._helper(root, 0)
        return self.balanced
    def _helper(self, root, height):
        if not self.balanced:
            return -1
        if not root:
            return 0
        leftHeight = self._helper(root.left, height)
        rightHeight = self._helper(root.right, height)
        if abs(leftHeight - rightHeight) > 1:
            self.balanced = False
            return -1
        return max(leftHeight, rightHeight) + 1