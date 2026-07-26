class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum()) #alnum because senetence contains special chr and not alp only ,so thats when join condition gets true
        left = 0 
        right = len(s) - 1

        while (left < right):
            if (s[left] != s[right]):
                return False
            else:

             left += 1
             right -= 1

        return True