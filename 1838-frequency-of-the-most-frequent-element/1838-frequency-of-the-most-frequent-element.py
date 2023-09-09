class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=0
        ans=0
        s=0
        for r in range(len(nums)):
            s+=nums[r]
            while s+k<nums[r]*(r-l+1):
                s-=nums[l]
                l+=1
            ans=max(ans,r-l+1)
        return ans