class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        seen = set()

        left = 0
        seen.add(s[0])

        maxLen = 1
        for right in range(1, len(s)):
            if s[right] in seen:
                while left < right and s[left] != s[right]:
                    seen.discard(s[left])
                    left += 1
                left += 1
                seen.discard(s[right])

            seen.add(s[right])
            maxLen = max(maxLen, right-left+1)
        
        return maxLen