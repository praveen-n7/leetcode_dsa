import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = [-c for c in Counter(tasks).values()]
        heapq.heapify(h)

        q = deque()
        t = 0

        while h or q:
            t += 1

            if h:
                c = -heapq.heappop(h) - 1
                if c > 0:
                    q.append((t + n, c))

            if q and q[0][0] == t:
                _, c = q.popleft()
                heapq.heappush(h, -c)

        return t