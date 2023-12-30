class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        mp={}
        for i in words:
            for j in i:
                if j in mp:
                    mp[j]+=1
                else:
                    mp[j]=1
        l=list(mp.values())
        for i in l:
            if i%len(words)==0:
                continue
            else:
                return 0
        return 1