# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def preorder(root):
            if not root:
                return False
            if (k - root.val) in seen:
                return True
            seen.add(root.val)
            return preorder(root.left) or preorder(root.right)

        return preorder(root)
