class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        vals=sorted(set(nums),reverse=True)
        return vals[2] if len(vals)>= 3 else vals[0]
        