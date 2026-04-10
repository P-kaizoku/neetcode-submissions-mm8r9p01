class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1
        
        sorted_mp = dict(sorted(mp.items(), key=lambda item:item[1], reverse=True))

        ans = list(sorted_mp.keys())[:k]
        return ans
        