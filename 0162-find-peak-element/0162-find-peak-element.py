class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        u=len(nums)-1
        while l<u:
            mid=(l+u)//2
            if nums[mid]>=nums[mid+1]:
                u=mid
            else:
                l=mid+1
        return l