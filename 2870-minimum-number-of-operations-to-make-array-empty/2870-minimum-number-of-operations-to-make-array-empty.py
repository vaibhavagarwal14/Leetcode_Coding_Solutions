class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        res=0
        for i in freq.values():
            if i==1:
                return -1
            else:
                res+=(i+2)//3
        return res