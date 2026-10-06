class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        def kadane_gain(a, b):
            current = 0
            best = 0

            for x, y in zip(a, b):
                current = max(0, current + y - x)
                best = max(best, current)

            return best

        gain1 = kadane_gain(nums1, nums2)
        gain2 = kadane_gain(nums2, nums1)

        return max(sum1 + gain1, sum2 + gain2)