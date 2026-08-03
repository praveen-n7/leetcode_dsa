class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        if len(s) != len(t):
            return False

        counter = {}

        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for char in t:
            if char not in counter or counter[char]==0 :#to handle repetition of characters so that so that if two char nedded and one is there that time also false 
                return False
            counter[char] -= 1

        return True