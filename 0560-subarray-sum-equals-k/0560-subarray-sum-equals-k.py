class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Approach 1 - BF
        # Approach 2 - BF better
        
        # Approach 3
        freq={}
        freq[0]=1
        s=0
        count=0
        for i in nums:
            s+=i
            if s-k in freq:
                count+=freq[s-k]
            if s in freq:
                freq[s]+=1
            else:
                freq[s]=1
        return count