# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #obseerve how in sequential or series the if logic is written to check first the most prior condition without jumping to least prior, notice the depth of logic 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # if both nodes doesnt exist return true
            return True
        if not p or not q: #either exist not same 
            return False
        if p.val!=q.val: #if nodes exists but values not same return false 
            return False 
        return(self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right)) # recuresilvely check for all nodes left and right if anyone also returns false the final answer is false 


        