class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        lst=[]
        i=0
        j=1
        count=0
        while i<len(target):
            if target[i]==j:
                while count>0:
                    lst.append("Pop")
                    count-=1
                lst.append("Push")
                i+=1
                j+=1
            else:
                count+=1
                lst.append("Push")
                j+=1
        return lst