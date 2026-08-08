# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Recursion is all about how you connect things to get the desired outcome for every tracking logic designed, its about what to return for what condition and what is the final return of the function, how does it recursively derive the final result of all,does the final value match the our problem pattern ?
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node): #check the node exists
            if not node:
                return 0 
            left_height=check(node.left) #check left node contracr
            if left_height==-1: #check if this node has failure value of that defines unbalance tree
                 return -1
            #return 1
            right_height=check(node.right)
            if right_height==-1: #check if this node has failure value of that defines unbalance tre
                  return -1
        #return 1
            if abs(left_height-right_height)>1:#this one assigns the failure values to nodes that defines unbalance of the tree
                  return -1 
            return 1+max(left_height,right_height) #max of left and right subtrees that agrees to the above conditions of the function
            #remember balance is the height should of subtree should be same or close/small difference is acceptable  
        return check(root)!=-1 #return true if not a failur value throughout the recursive call of the check node which is a contract node 


        #NOTE obserive how each condition is applied in sequence and series to meet the required pattern logic 
        