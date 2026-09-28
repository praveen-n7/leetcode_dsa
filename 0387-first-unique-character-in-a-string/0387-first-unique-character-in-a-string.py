from collections import Counter,deque
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        q=deque(range(len(s)))
        while q and count[s[q[0]]]>1:
            q.popleft()
        return q[0] if q else -1

        