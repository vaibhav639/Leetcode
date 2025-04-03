# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)

        new_root = TreeNode(arr[0])
        curr = new_root
        for val in arr[1:]:
            curr.right = TreeNode(val)
            curr = curr.right
        return new_root
                
                
                