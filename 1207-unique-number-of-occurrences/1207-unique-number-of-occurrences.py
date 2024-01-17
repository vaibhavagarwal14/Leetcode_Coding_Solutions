class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp={}
        for i in arr:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        s=set()
        for i in mp.values():
            s.add(i)
        return len(s)==len(mp.values())