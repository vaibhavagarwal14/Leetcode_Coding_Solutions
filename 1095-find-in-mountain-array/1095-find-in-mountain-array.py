# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findpeak(self,A,l,u):
        while(l<u):
            mid=(l+u)//2
            if(A.get(mid)<A.get(mid+1)):
                l=mid+1
            else:
                u=mid
        return l
    def findleft(self,A,t,l,u):
        while(l<u):
            mid=(l+u)//2
            if(A.get(mid)<t):
                l=mid+1
            else:
                u=mid
        return l
    def findright(self,A,t,l,u):
        while(l<u):
            mid=(l+u)//2
            if(A.get(mid)>t):
                l=mid+1
            else:
                u=mid
        return l
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n=mountain_arr.length()
        peak=self.findpeak(mountain_arr,0,n-1)
        left=self.findleft(mountain_arr,target,0,peak)
        if mountain_arr.get(left)==target:
            return left
        right=self.findright(mountain_arr,target,peak+1,n-1)
        if mountain_arr.get(right)==target:
            return right
        return -1
            