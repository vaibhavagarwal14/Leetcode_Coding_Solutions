class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=0
        u=len(nums)-1
        while(l<u):
            if(nums[l]%2==1 and nums[u]%2==0):
                nums[l],nums[u]=nums[u],nums[l]
                l+=1
                u-=1
            elif(nums[l]%2==1 and nums[u]%2==1):
                u-=1
            elif(nums[l]%2==0 and nums[u]%2==0):
                l+=1
            else:
                l+=1
        return nums