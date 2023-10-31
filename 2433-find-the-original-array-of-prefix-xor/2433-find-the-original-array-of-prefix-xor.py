class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        lst=[]
        lst.append(pref[0])
        xor=pref[0]
        for i in range(1,len(pref)):
            lst.append(xor^pref[i])
            xor=pref[i]
        return lst