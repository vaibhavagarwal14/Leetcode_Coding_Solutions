class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1 - BF - Generate all permutations and then see O(n!*n)
        
        # Approach 2 O(3n)
        def reverse(nums,l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
                
        n = len(nums)
        ind=-1
        
        # Part 1 - find index until which the prefix will remain same
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        if ind==-1:
            reverse(nums,0,n-1)
            return
        
        # Part 2 - find the element > nums[ind] but minimum in remaining
        for i in range(n-1,ind,-1):
            if nums[i]>nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
                break
        
        # Part 3 - reverse the array after ind to get minimum value of that array
        reverse(nums,ind+1,n-1)