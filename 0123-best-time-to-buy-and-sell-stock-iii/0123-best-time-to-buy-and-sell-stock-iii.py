class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sellone=selltwo=0
        holdone=holdtwo=-math.inf
        for p in prices:
            selltwo=max(selltwo,holdtwo+p)
            holdtwo=max(holdtwo,sellone-p)
            sellone=max(sellone,holdone+p)
            holdone=max(holdone,-p)
        return selltwo
        