class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1
        
        mp1 = dict(sorted(mp.items(), key=lambda x:x[1], reverse=True)
)
        return list(mp1.keys())[:k]