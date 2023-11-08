class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        minstep=max(abs(sx-fx),abs(sy-fy))
        if minstep==0:
            return t!=1
        else:
            return minstep<=t