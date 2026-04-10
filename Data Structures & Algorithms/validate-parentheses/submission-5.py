class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        brackets = {"]":"[", "}":"{", ")":"("}

        for b in s:
            if b in brackets:
                if not st or st.pop() != brackets[b]:
                    return False
            else:
                st.append(b)
                
        return len(st)==0