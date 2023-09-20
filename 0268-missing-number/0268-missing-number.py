class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Approach 1 (Optimal)
        # n=len(nums)
        # s=sum(nums)
        # return (n*(n+1)//2)-s
        
        # Approach 2 (optimal-better)
        xor1=0
        xor2=0
        for i in range(len(nums)):
            xor1^=i+1
            xor2^=nums[i]
        return xor1^xor2