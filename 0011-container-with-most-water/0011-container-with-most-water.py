class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx=0
        f=0
        s=len(height)-1
        while(f<s):
            ar=min(height[f],height[s])*(s-f)
            if(ar>mx):
                mx=ar
            if(height[f]>height[s]):
                s-=1
            else:
                f+=1
        return mx  
