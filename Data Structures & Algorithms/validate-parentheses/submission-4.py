class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        brackets = {"]":"[", "}":"{", ")":"("}

        for b in s:
            if st and b in brackets.keys():
                if brackets[b] != st.pop():
                    return False
            else:
                st.append(b)
                
        return len(st)==0