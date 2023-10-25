class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k==1:
            return 0
        if k&1:
            return int(self.kthGrammar(n-1,(k+1)//2)!=0)
        return int(self.kthGrammar(n-1,(k+1)//2)==0)