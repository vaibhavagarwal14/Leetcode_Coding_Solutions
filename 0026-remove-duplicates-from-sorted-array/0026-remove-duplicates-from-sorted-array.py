class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num=[]
        i=0
        while i < len(nums):
            if nums[i] in num:
                nums.remove(nums[i])
            else:
                num.append(nums[i])
                i+=1
        return (len(num))