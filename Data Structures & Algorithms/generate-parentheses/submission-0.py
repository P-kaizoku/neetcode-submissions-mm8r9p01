class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        paran = ""

        def backtrack(open, close):
            nonlocal paran
            if open == n and close == n:
                res.append(paran)
            
            if open < n:
                paran += "("
                backtrack(open+1, close)
                paran = paran[:-1]

            
            if close < open:
                paran += ")"
                backtrack(open, close+1)
                paran = paran[:-1]
           
        backtrack(0, 0)
        return res
        