class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        u=len(nums)-1
        while l<u:
            mid=(l+u)//2
            if nums[mid]>nums[u]:
                l=mid+1
            else:
                u=mid
        return nums[l]