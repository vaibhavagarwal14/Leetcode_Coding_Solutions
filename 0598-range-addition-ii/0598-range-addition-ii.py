class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minx=m
        miny=n
        for i,j in ops:
            minx=min(minx,i)
            miny=min(miny,j)
        return minx*miny