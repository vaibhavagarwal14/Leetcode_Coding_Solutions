class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        mx=max(count.values())
        if mx > len(nums)/2:
            for key in count.keys():
                if count[key]==mx:
                    return key