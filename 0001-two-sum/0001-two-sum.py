class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach 1 - Brute Force
        # lst=[]
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]+nums[j]==target):
        #             lst.append(i)
        #             lst.append(j)
        #             break
        # return lst
        
        #Approach 2 - Hashing
        count={}
        for i in range(len(nums)):
            if target-nums[i] in count:
                return [i,count[target-nums[i]]]
            count[nums[i]]=i
        