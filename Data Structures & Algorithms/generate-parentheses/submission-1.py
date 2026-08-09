class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        paran = []

        def backtrack(open, close):
            nonlocal paran
            if open == n and close == n:
                res.append("".join(paran))
            
            if open < n:
                paran.append("(")
                backtrack(open+1, close)
                paran = paran[:-1]

            
            if close < open:
                paran.append(")")
                backtrack(open, close+1)
                paran = paran[:-1]
           
        backtrack(0, 0)
        return res
        