from collections import deque

class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)
        P = [0] * (n + 1)

        for i, v in enumerate(nums):
            P[i + 1] = P[i] + v

        dq = deque()
        best = float('inf')

        for i in range(n + 1):
            while dq and P[i] - P[dq[0]] >= k:
                best = min(best, i - dq.popleft())

            while dq and P[i] <= P[dq[-1]]:
                dq.pop()

            dq.append(i)

        return -1 if best == float('inf') else best