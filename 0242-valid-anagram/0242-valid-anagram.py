class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd={}
        for i in s:
            if i in sd:
                sd[i]+=1
            else:
                sd[i]=1
        for i in t:
            if i in sd:
                sd[i]-=1
            else:
                return False
        if max(sd.values())==0 and min(sd.values())==0:
            return True
        return False