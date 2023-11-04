class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if len(left)==0 and len(right)==0:
            return 0
        if len(right)==0:
            return max(left)
        if len(left)==0:
            return n-min(right)
        return max(max(left),n-min(right))