class Solution:
    def isValid(self, s: str) -> bool:

        mp = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        } 


        stack = []

        for c in s:
            if c in mp.keys() and stack and stack[-1] == mp[c]:
                stack.pop()
                continue
            

            stack.append(c)
        
        return stack == []