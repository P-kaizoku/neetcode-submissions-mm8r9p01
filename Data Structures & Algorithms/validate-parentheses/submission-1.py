class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {"}":"{", ")":"(", "]":"["}

        for p in s:
            if p in mp.values():
                stack.append(p)
            elif not stack or stack.pop()!=mp[p]:
                return False
        
        return not stack



             