class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Approach 1 - BF
        p=[]
        n=[]
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        for i in range(len(nums)//2):
            nums[2*i]=p[i]
            nums[2*i+1]=n[i]
        return nums