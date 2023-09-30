class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        l=0
        i=0
        while i < len(s):
            l+=1
            lim=0
            while(lim<100 and i<len(s)):
                w=widths[ord(s[i])-97]
                if lim+w<=100:
                    i+=1
                    lim+=w
                else:
                    break
            if i==len(s):
                return [l,lim]
            