# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._inorderHelper(root, result)
        return result

    def _inorderHelper(self, root, result):
        if not root:
            return
        self._inorderHelper(root.left, result)
        result.append(root.val)
        self._inorderHelper(root.right, result)