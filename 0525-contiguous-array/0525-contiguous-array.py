class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0: -1}
        s = best = 0
        for i, v in enumerate(nums):
            s += -1 if v == 0 else 1
            if s in first:
                best = max(best, i - first[s])
            else:
                first[s] = i
        return best