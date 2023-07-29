class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # store={}
        # for i in range(len(s)):
        #     if t[i] in store.values() and s[i] not in store.keys():
        #         return False
        #     elif s[i] not in store:
        #         store[s[i]]=t[i]
        #     else:
        #         if t[i]!=store[s[i]]:
        #             return False
        # return True
        return [*map(s.index,s)]==[*map(t.index,t)]