class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Approach 1 - BF O(2n)
        # p=[]
        # n=[]
        # for i in nums:
        #     if i>0:
        #         p.append(i)
        #     else:
        #         n.append(i)
        # for i in range(len(nums)//2):
        #     nums[2*i]=p[i]
        #     nums[2*i+1]=n[i]
        # return nums
        
        # Approach 2 - Using O(n)
        arr=[0]*len(nums)
        p=0
        n=1
        for i in nums:
            if i>0:
                arr[p]=i
                p+=2
            else:
                arr[n]=i
                n+=2
        return arr