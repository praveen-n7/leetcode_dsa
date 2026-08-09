# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
             return [] #empty root return empty list
        result =[]
        queue=[root]# root first processing thats why queue is used 
        while queue: #as long as leaf isnt reached keep on appending queue
              level=[] #correct declaration of this to control the appending of list inside listb values 
              for _ in range(len(queue)):#range determines the node has child or not and tells when to stop for every node 
                  #level=[] #wrong scope 
            
                  node=queue.pop(0) #pop first element because fisrst in first out queue
                  level.append(node.val) 
                  #check if it has childs and store them in queue, remeber check the question first left and then right appending accoridng to that if logic is designed 
                  if node.left:
                       queue.append(node.left)
                  if node.right:
                       queue.append(node.right)
              result.append(level)# append to original list the level elements
        return result
        