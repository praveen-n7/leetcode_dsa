class KthLargest:
    #min heap logic isused min element stays atv root

    def __init__(self, k: int, nums: List[int]):
        self.h=[]
        self.k=k
        for v in nums: self.add(v) #iterate via elements and use add logic condition to build the heap 
        

    def add(self, val: int) -> int:
        if (len(self.h)<self.k):#stay at the window goven kth 
            heapq.heappush(self.h,val)
        elif self.h[0]<val:#if new largest val than root  pop the root element  and replace new element at the end, now root becomes the min value in this window 
            heapq.heapreplace(self.h,val)
        return self.h[0] #return the root when above condition doesnt hit this value gets stored in the param_1 thishappens thriughout the array
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)