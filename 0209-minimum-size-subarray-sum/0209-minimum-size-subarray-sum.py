class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=sum(nums)
        if(s<target):
            return 0
        if(s==target):
            return len(nums)
        if(max(nums)>=target):
            return 1
        end=0
        start=0
        cs=0
        mn=len(nums)+1
        while end<len(nums):
            while(cs<target and end<len(nums)):
                cs+=nums[end]
                end+=1
            while (cs>=target and start<len(nums)):
                if(end-start<mn):
                    mn=end-start
                cs-=nums[start]
                start+=1
        return mn