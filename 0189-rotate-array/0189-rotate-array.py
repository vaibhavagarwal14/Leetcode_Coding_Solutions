class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1
        n=len(nums)
        k=k%n
        lst=[]
        for i in range(n-k,n):
            lst.append(nums[i])
        for i in range(n-k):
            lst.append(nums[i])
        for i in range(n):
            nums[i]=lst[i]
        
        
        
        
#         def reverse (nums,l,r):
#             while l<r:
#                 nums[l],nums[r]=nums[r],nums[l]
#                 l+=1
#                 r-=1
        
#         k%=len(nums)
#         reverse(nums,0,len(nums)-1)
#         reverse(nums,0,k-1)
#         reverse(nums,k,len(nums)-1)