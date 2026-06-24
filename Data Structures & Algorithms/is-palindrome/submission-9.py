class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '')
        end = len(s) - 1
        for i in range(len(s)):
            if not s[i].isalnum() or s[i] == ' ' or s[end] == ' ':
                continue
            if not s[end].isalnum():
                end -= 1
            if s[i].lower() == s[end].lower():
                end -= 1
            else: 
                return False

        return True
    