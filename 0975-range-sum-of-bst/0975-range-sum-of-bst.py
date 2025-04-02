# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ = 0
        def preorder(root):
            nonlocal summ
            if not root:
                return
            value = root.val
            if value >= low and value <= high:
                summ+=value
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return summ
        
        