# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) #create dummy node 
        tail=dummy
        while list1 and list2: #list must be true ie should exist 
            if list1.val<=list2.val: #compare values
                tail.next,list1=list1,list1.next #insert the desired node using tail.next and not tail only and then dont forget further connection of the list 
            else:
                tail.next,list2 = list2,list2.next #same here
            tail=tail.next
        tail.next = list1 or list2 #make tail.next the last node of either of the list (because one may be smaller one may be big so thats why or )
        return dummy.next #return the dummy.next which is head

        #final intution linked lists are not continous array they are linked via addresses of nodes (next and prev)
        