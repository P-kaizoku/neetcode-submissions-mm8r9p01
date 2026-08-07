class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(idx, combi, curr_sum):
            if curr_sum == target:
                res.append(combi.copy())
                return
            

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                if curr_sum + candidates[i] > target:
                    continue
                
                combi.append(candidates[i])
                backtrack(i+1, combi, curr_sum+candidates[i])

                combi.pop()
            
        backtrack(0, [], 0)
        return res
