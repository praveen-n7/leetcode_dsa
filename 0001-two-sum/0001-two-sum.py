class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, num in enumerate(nums):
            need = target-num
            if need in seen:
                return [i,seen[need]]
            seen[num]=i
        return []


        