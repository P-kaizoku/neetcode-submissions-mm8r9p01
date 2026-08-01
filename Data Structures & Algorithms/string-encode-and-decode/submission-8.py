class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            n = str(len(s))
            res += n + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            n = 0
            while s[i] != "#":
                n = (10*n)+int(s[i])
                i += 1
            
            res.append(s[i+1:n+i+1])
            i = n+i+1
            
        return res
