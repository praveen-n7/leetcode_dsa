class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen=set()
        for right,v in enumerate(nums):
            if v in  seen: #values matches with vale in set
                return True
            seen.add(v)  #not seen values added in set
            if(len(seen)>k):
                seen.discard(nums[right-k]) #no third distinct element discard the value of nums of the left of the window from the set
        return False

        