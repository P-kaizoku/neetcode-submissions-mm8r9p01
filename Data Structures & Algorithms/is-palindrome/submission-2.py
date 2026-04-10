class Solution:
    def getAlphaNumStr(self, s: str) -> str:
        result = ""

        for c in s:
            if c.isalnum():
                result += c.lower()

        return result
    def isPalindrome(self, s: str) -> bool:
        
        validStr = self.getAlphaNumStr(s)

        return validStr == validStr[::-1]