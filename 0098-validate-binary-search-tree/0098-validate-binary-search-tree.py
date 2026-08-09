# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,min_val,max_val): #recursion logic the main logic is alsways at the end the above is the control logic with base condition
            if not node:
                return True #base condition
            if node.val<=min_val or node.val>=max_val:#setting range of the left and right nodes 
                return False #failue condition
            return validate(node.left,min_val,node.val) and validate(node.right,node.val,max_val) #recursion calls 
        return validate(root,float ('-inf'),float ('inf'))# real arguments for starting the process 

        #NOTE the indentation of the functiojn inside the function check returns at each indentation and also obeserve how negative and positive ranges are defined using float inf ith appropriate signs for approppriate arguments 
        