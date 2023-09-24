class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Approach 1 - Brute Force
        
        # Approach 2 - Kadane's Algorithm
        s=0
        mx=nums[0]
        for i in nums:
            s+=i
            mx=max(mx,s)
            if s<0:
                s=0
        return mx