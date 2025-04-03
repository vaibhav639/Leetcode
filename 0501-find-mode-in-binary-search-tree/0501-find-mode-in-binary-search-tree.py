# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)

        freq = {}

        for num in arr:
            freq[num] = freq.get(num,0) + 1
        
        max_freq = max(freq.values())
        modeList = [key for key,val in freq.items() if val == max_freq]

        return modeList

        