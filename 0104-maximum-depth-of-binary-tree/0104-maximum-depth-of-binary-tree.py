# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 #base conditin for recursion

        #left=max(self.maxDepth(root.left)) wrong max fun remove wrong intution max used at end to return max of left and right node

        left=(self.maxDepth(root.left))#recursive call till depth is reached
        right=(self.maxDepth(root.right))
        return 1+max(left,right) #oce the base condition is hit the result of every node recursively called start getting accumulated and computing with each other according to the logic designed 
        