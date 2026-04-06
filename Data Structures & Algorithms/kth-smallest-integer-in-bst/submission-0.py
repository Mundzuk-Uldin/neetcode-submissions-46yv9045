class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        res = -1
        def getKthSmallest(root):
            nonlocal i, res
            if not root or res != -1:
                return
            getKthSmallest(root.left)
            i += 1
            if i == k:
                res = root.val
                return
            getKthSmallest(root.right)
        getKthSmallest(root)
        return res