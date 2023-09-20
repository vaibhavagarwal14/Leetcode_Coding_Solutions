class Solution:
    def check(self, nums: List[int]) -> bool:
        f=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                f+=1
        if (f==1 and nums[-1]<=nums[0]) or f==0:
            return 1
        return 0