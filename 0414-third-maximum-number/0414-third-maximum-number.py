class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1=m2=m3=-(2**31)-1
        for i in nums:
            if i>m1:
                m3=m2
                m2=m1
                m1=i
            elif m1>i and i>m2:
                m3=m2
                m2=i
            elif m2>i and i>m3:
                m3=i
        if m3==-(2**31)-1:
            return m1
        return m3
            