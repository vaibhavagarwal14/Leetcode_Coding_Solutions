class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Approach 1
        # num=[]
        # i=0
        # while i < len(nums):
        #     if nums[i] in num:
        #         nums.remove(nums[i])
        #     else:
        #         num.append(nums[i])
        #         i+=1
        # return (len(num))
        
        # Approach 2
        i=0
        for num in nums:
            if i<1 or num>nums[i-1]:
                nums[i]=num
                i+=1
        return i