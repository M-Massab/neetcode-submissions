class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s) - 1
        i = 0
        s = s.lower()
        
        while i <= n:
            # Change this: Check if it's NOT a letter or number
            if not s[i].isalnum():
                i = i + 1
                continue
                
            # Change this: Check if it's NOT a letter or number
            if not s[n].isalnum():
                n = n - 1
                continue
                
            if s[i] == s[n]:
                i = i + 1
                n = n - 1
            else:
                return False
        return True
