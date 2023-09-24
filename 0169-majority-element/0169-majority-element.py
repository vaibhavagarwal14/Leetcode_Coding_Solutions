class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach 1 - Hashing
        # count={}
        # for i in nums:
        #     if i not in count:
        #         count[i]=1
        #     else:
        #         count[i]+=1
        # mx=max(count.values())
        # if mx > len(nums)/2:
        #     for key in count.keys():
        #         if count[key]==mx:
        #             return key
        
        # Approach 2 - Moore's Voting Algorithm
        ans=0
        count=0
        for i in nums:
            if count==0:
                ans=i
            if ans==i:
                count+=1
            else:
                count-=1
        return ans