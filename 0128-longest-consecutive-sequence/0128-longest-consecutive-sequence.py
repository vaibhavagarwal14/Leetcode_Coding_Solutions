class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Approach 1 - BF O(n^2)
        # Approach 2 - Sort O(nlogn+n)
        
        # Approach 3 O(3n)
        if len(nums)==0:
            return 0
        s=set()
        for i in nums:
            s.add(i)
        longest=1
        for i in s:
            if i-1 not in s:
                count=1
                x=i
                while x+1 in s:
                    count+=1
                    x+=1
                longest=max(longest,count)
        return longest