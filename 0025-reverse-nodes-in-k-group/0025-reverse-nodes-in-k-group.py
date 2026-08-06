# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        vals=[] #create new space 
        #store values in the space of nodes 
        while head:
            vals.append(head.val)
            head=head.next
        #logic control using loop,understand how loop is customized according to the need with proper increment and how thingd are being reversed at each stage 
        for i in range(0,len(vals)-len(vals)%k,k):
            vals[i:i+k]=reversed(vals[i:i+k]) #array slicing technique 
        dummy = ListNode(0) #create instance of dummy node 
        tail =  dummy 
        #start connecting values by creating nodes and linking them respectiveky  
        for v in vals:
            tail.next=ListNode(v)
            tail=tail.next
        return dummy.next #return the first node which eventually is connected at bigger picture for our desired result 

        