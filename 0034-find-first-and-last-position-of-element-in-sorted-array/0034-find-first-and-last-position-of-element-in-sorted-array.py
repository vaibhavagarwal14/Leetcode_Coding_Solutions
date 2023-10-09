class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Approach 1 - BF - O(n)
        
        # Approach 2 - BS - O(2*logn)
        
        # Approach 3 - BS - O(logn)
        l=0
        u=len(nums)-1
        if u==-1:
            return [-1,-1]
        while l<=u:
            mid=(l+u)//2
            if nums[mid]==target:
                i=mid
                j=mid
                while(i<len(nums)-1 and nums[mid]==nums[i+1]):
                    i+=1
                while(j>0 and nums[mid]==nums[j-1]):
                    j-=1
                return [j,i]
            elif nums[mid]<target:
                l=mid+1
            else:
                u=mid-1
        return [-1,-1]