# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # focus on the cases and also observe no loops are used its pure recursion
        if not root: # if not node (base condition)
            return 0 
        if not root.left: #if only right child present 
            return 1+(self.minDepth(root.right))
        if not root.right: #if only left child is present 
            return 1+(self.minDepth(root.left))
        return 1+min(self.minDepth(root.left),self.minDepth(root.right)) #if both child are present 
        