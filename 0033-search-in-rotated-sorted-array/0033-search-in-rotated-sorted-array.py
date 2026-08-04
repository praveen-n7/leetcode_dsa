class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #its all about getting intution of moving the index by comparing range with logic moving the boundary index accordingly to make sure every mid in that range is touched and compared with conditions
        left =0 
        right =len(nums)-1
        while(left<=right):
            mid=left+(right-left)//2
            if(nums[mid]==target):
                return mid
            #if(nums[left]<nums[right]): wrong 
            if(nums[left]<=nums[mid]):#comparision happemimg with mid value not right value

                 if(nums[left]<=target<nums[mid]):#if mid is max and target between left nd mid
                     right=mid-1
                 else:
                      left=mid+1 #target <mid
            else:#when left > right
                if(nums[mid]<target<=nums[right]):# again check where target lie and move left or right accordingly 
                    left=mid+1
                else:
                    right=mid-1
        return -1
        # so basically its rotated sorted arraay so left and right comparison is must to find the serach of target at every iteration(imp point)
            
        