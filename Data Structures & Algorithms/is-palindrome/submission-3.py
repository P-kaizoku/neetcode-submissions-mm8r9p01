class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def clean(s: str) -> str:
            res = ""

            for c in s:
               if c.isalnum():
                res += c.lower()
            
            return res
        
        s = clean(s)

        return s == s[::-1]
