# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals=[] #new space to store the results 
        for head in lists: #list of lists
            while head: #each list as index of lists 
                vals.append(head.val)#storing every value in new space 
                head=head.next #moving index of list inside lists 
        vals.sort() #sorting everything 
        dummy =ListNode(0)#linking everything 
        tail=dummy
        for v in vals:
            #tail.next=v wrong instance must be created
            tail.next=ListNode(v) #dont forget to create instance of the node and store the v value as value of that node 
            tail=tail.next #link all the nodes 
        return dummy.next

        