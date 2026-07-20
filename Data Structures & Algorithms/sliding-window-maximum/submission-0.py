class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        if k==1:
            return nums
        
        dq = deque()
        result = []
        n = len(nums)
        for i in range(n):

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)


            if dq[0] == i-k:
                dq.popleft()
            

            if i >= k-1:
                result.append(nums[dq[0]])

        return result