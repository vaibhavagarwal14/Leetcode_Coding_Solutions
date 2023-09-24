class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn=prices[0]
        prf=0
        for i in range(1,len(prices)):
            cost=prices[i]-mn
            prf=max(prf,cost)
            mn=min(mn,prices[i])
        return prf