class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = set()

        for i in range(len(nums)):
            tar = -nums[i]
            mp = {}

            for j in range(i+1, len(nums)):
                diff = tar - nums[j]

                if diff in mp:
                    trip = tuple(sorted([diff, nums[i], nums[j]]))
                    ans.add(trip)
                
                mp[nums[j]] = j
        
        return [x for x in ans]