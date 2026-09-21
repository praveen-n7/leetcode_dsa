class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer = [0]*n
        for i in range(n):
            L=sum(nums[:i])
            R=sum(nums[i+1:])
            answer[i]=abs(L-R)
        return answer
        