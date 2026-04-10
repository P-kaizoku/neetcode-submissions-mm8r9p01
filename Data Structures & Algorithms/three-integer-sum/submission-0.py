class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        for i in range(len(nums)):
            target = -nums[i]
            hashset = set()

            for j in range(i+1, len(nums)):
                diff = target - nums[j]
                if diff in hashset:
                    tuplet = tuple(sorted([diff, nums[j], nums[i]]))
                    ans.add(tuplet)
                hashset.add(nums[j])
            
        return [list(tuplet) for tuplet in ans]