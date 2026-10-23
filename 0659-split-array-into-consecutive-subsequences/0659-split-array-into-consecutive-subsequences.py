import heapq
from collections import defaultdict

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        m = defaultdict(list)

        for v in nums:
            if m[v - 1]:
                L = heapq.heappop(m[v - 1])
                heapq.heappush(m[v], L + 1)
            else:
                heapq.heappush(m[v], 1)

        for h in m.values():
            if h and h[0] < 3:
                return False

        return True