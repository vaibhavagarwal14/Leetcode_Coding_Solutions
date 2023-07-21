class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=2
        while(i<n):
            if(nums[i]==nums[i-1] and nums[i]==nums[i-2]):
                nums.pop(i)
                n-=1
            else:
                i+=1
        return len(nums)