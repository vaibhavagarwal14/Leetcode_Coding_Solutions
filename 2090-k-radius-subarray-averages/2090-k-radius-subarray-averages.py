class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avg=[-1]*len(nums)
        if k>len(nums):
            return avg
        s=sum(nums[:2*k+1])
        for i in range(k,len(nums)-k):
            avg[i]=s//(2*k+1)
            if(i+k+1<len(nums)):
                s+=nums[i+k+1]-nums[i-k]
        return avg