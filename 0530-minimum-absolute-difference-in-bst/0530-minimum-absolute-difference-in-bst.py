# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def preorder(root):
            if not root:
                return
            arr.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)

        arr.sort()
        
        mn = float("inf")

        for i in range(1,len(arr)):
            mn = min(mn, arr[i]-arr[i-1])

        return mn




            
