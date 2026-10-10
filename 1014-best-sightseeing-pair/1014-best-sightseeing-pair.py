class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        bestLeft = values[0] + 0
        best = 0

        for j in range(1, len(values)):
            best = max(best, bestLeft + values[j] - j)
            bestLeft = max(bestLeft, values[j] + j)

        return best