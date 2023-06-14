class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst=[]
        nums.sort()
        for i in range(0,len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            l=i+1
            r=len(nums)-1
            while(l<r):
                s=nums[i]+nums[l]+nums[r]
                if(s<0):
                    l+=1
                elif(s>0):
                    r-=1
                else:
                    lst.append([nums[i],nums[l],nums[r]])
                    while l<len(nums)-1 and nums[l]==nums[l+1]:
                        l+=1
                    while r>0 and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return lst