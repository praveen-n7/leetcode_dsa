# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur,prev=head,None #initial cur and prev , prev will be following cur and linking reverse
        while cur:
            nxt=cur.next #to store next vale of cur.next 
            cur.next=prev #break cur.next and link it with prev node so that it becomes reverse  
            prev,cur=cur,nxt #update values to move further with same logic and pattern till end if loop condition
        return prev # prev after end will be pointing at last node which is reverse linked compared to original
        