import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = [1]
        seen = {1}
        last = 1

        for _ in range(n):
            last = heapq.heappop(h)
            for p in (2, 3, 5):
                x = last * p
                if x not in seen:
                    seen.add(x)
                    heapq.heappush(h, x)

        return last