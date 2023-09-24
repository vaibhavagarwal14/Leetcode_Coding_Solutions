class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1 - Sort
        
        # Approach 2 - use counters
        # c=[0,0,0]
        # for i in nums:
        #     if i == 0:
        #         c[0]+=1
        #     elif i == 1:
        #         c[1]+=1
        #     else:
        #         c[2]+=1
        # for i in range(c[0]):
        #     nums[i]=0
        # for i in range(c[1]):
        #     nums[i+c[0]]=1
        # for i in range(c[2]):
        #     nums[i+c[0]+c[1]]=2
        
        # Approach 3 - DNF
        low=0
        mid=0
        h=len(nums)-1
        while(mid<=h):
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[h]=nums[h],nums[mid]
                h-=1
        