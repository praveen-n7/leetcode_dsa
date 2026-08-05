# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head) #linking the given node in the argument of the function
        fast=slow=dummy
        for _ in range(n+1):
            fast=fast.next #creates the difference in moment so that slow gets the targetted node 
        while fast:#last value of the list which is not none 
             fast=fast.next
             slow=slow.next
             #at the end of the loop slow gets the node before target 
        slow.next=slow.next.next
        return dummy.next #return head