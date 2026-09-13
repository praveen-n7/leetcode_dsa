# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next
        prev,cur =None,slow
        while cur :
            nxt = cur.next
            cur.next=prev
            prev,cur=cur,nxt
        while prev:
            if head.val != prev.val:
                return False
            head,prev = head.next,prev.next
        return True
        