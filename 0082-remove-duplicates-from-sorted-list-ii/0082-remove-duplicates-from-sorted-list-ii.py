# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head) #initialization of dummy node
        prev=dummy #prev pointing to dummy node to track unique nodesand not duplicates 
        while head:
            if head.next and head.val == head.next.val: #compare head next values with current node
                while head.next and head.val==head.next.val:#run the scan till we find unique node 
                    head=head.next
                prev.next=head.next#point the unique node to next of prev which is currently pointing to dummy 
            else:
                prev=prev.next# link prev next if not duplicate node 
            head = head.next #update head
        return dummy.next #return dummy next which is pointing head 
        