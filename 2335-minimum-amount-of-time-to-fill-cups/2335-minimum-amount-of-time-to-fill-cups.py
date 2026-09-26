import heapq
class Solution:
    def fillCups(self, amount: list[int]) -> int:
        h = [-v for v in amount if v > 0]
        heapq.heapify(h)
        t = 0
        while len(h) >= 2:
          x = -heapq.heappop(h) - 1
          y = -heapq.heappop(h) - 1
          if x > 0: heapq.heappush(h, -x)
          if y > 0: heapq.heappush(h, -y)
          t += 1
        if h: t += -heapq.heappop(h)
        return t

        