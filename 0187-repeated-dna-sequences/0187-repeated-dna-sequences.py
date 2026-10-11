class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        k = 10
        seen, dup = set(), set()
        for i in range(len(s) - k + 1):
            win = s[i:i + k]
            if win in seen:
                dup.add(win)
            else:
                seen.add(win)
        return list(dup)