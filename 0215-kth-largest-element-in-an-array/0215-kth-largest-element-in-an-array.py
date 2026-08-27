class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[] #min heap usage the top of the heap will give us the req answer if correct logic applied wrt k  
        for v in nums:
            heapq.heappush(h,v)
            if len(h)>k:heapq.heappop(h) #pops up the smaller element which is at root amd moves next smaller element to the root if len h goes out of range
        return h[0] #return root node ie the smallest of all highest asked in k range 
        