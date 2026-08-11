# we use max heap pattern, since there is no mx heap we nuse min heap and store values as negative so the  max value is at the root, but while computing or return result we use minus sign to make it positive and return the actual value intead of stored negative values 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=[-s for s in stones] #stroting as negaitive values
        heapq.heapify(h)
        while(len(h)>1): #running the loop until one elements is remained 
            y=-heapq.heappop(h) #y is the first outer or downoward element near tye boundary
            x=-heapq.heappop(h)# x is second next boundary element from the right side 
           # y=-heapq.heappop(h) mistake first y then x 
            if y>x : heapq.heappush(h,-(y-x)) #remember while computing usenegative signs to compensate with min heap 
        return -h[0] if h else 0 #retun the root element of the heap
        