class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Approach 1 - BF
        # Approach 2 - Hashing 
        
        # Approach 3 - Extended Moore's Algorithm
        c1=0
        c2=0
        e1=None
        e2=None
        for i in nums:
            if c1==0 and e2!=i:
                c1+=1
                e1=i
            elif c2==0 and e1!=i:
                c2+=1
                e2=i
            elif e1==i:
                c1+=1
            elif e2==i:
                c2+=1
            else:
                c1-=1
                c2-=1
        c1=0
        c2=0
        for i in nums:
            if e1==i:
                c1+=1
            if e2==i:
                c2+=1
        lst=[]
        if c1>len(nums)/3:
            lst.append(e1)
        if c2>len(nums)/3:
            lst.append(e2)
        return lst