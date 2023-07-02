class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=[0,0,0]
        for i in nums:
            if i == 0:
                c[0]+=1
            elif i == 1:
                c[1]+=1
            else:
                c[2]+=1
        for i in range(c[0]):
            nums[i]=0
        for i in range(c[1]):
            nums[i+c[0]]=1
        for i in range(c[2]):
            nums[i+c[0]+c[1]]=2
        