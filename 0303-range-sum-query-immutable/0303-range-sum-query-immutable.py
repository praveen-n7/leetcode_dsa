class NumArray:

    def __init__(self, nums: List[int]):
        self.pre=[0]*(len(nums)+1) #creating array of one size bigger and initializing it with zero,so thAT 1st index doesnt get ignored
        for i ,v in enumerate(nums):
            self.pre[i+1]=self.pre[i]+v #adding prev and current and storing it in index 1 becuase index 0 is 0 to handle edge cases

        

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right+1]-self.pre[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)