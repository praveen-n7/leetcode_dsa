class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for col in range(len(strs[0])):
            ch = strs[0][col]
            for row in range(1,len(strs)):
                if col == len(strs[row]) or strs[row][col] != ch:
                    return strs[0][:col]
        return strs[0]
        