# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #dummy=ListNode(0)
        fast=slow=head #point fast and slow  directly to head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next# fast adn slow pointer logic 
            
            if fast == slow: 
                return True
        return False 
        
        
        