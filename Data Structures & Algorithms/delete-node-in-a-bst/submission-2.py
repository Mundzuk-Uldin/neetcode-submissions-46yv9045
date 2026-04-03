# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            else:
                minValRightSubtree = self._findMinBSTValue(root.right, key)
                root = self.deleteNode(root, minValRightSubtree)
                root.val = minValRightSubtree
        return root
    def _findMinBSTValue(self, root, key)-> int:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr.val
