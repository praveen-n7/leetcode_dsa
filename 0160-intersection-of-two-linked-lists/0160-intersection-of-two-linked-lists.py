# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p,q=headA,headB #point the pointers to both listnode s head 
        while p is not q: #the loop continues until an intersection is found
            p=p.next if p else headB #moving of pointer after every itertion and also this conditions take care if no intersection found or end of node with no intersection found also both pointers traverse both lists and compensate the length until they find p=q and also in case of no intersection p and q both meet at  none and return 0
            q=q.next if q else headA
        return p #return p if found 
        