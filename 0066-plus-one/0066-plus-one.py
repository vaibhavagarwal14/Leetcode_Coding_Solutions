class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        for i in digits:
            n=n*10+i
        n=n+1
        s=str(n)
        lst=[]
        for i in s:
            lst.append(int(i))
        return lst