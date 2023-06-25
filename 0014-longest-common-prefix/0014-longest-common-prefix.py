class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens=[]
        for i in strs:
            lens.append(len(i))
        mn=min(lens)
        n=len(strs)
        s=""
        for i in range(mn):
            d=strs[0][i]
            c=0
            for j in strs:
                if(j[i]==d):
                    c+=1
            if(c==n):
                s+=d
            else:
                break
        return s