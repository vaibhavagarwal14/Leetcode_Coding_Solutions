class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res=[]
        for i in range(len(bank)):
            if bank[i].count('1')!=0:
                res.append(bank[i].count('1'))
        if len(res)<=1:
            return 0
        op=0
        for i in range(1,len(res)):
            op+=res[i]*res[i-1]
        return op