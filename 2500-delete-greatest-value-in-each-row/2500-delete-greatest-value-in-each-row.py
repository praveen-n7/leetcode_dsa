import heapq
class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        heaps = [[-v for v in row] for row in grid]
        for h in heaps: heapq.heapify(h)
        ans = 0
        for _ in range(len(grid[0])):
            m = 0
            for h in heaps: m = max(m, -heapq.heappop(h))
            ans += m
        return ans
        