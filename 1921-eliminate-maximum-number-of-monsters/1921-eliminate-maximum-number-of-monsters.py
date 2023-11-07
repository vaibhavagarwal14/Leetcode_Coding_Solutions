class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        lst=[]
        for i in range(len(dist)):
            g=(dist[i]-1)//speed[i]
            lst.append(g)
        lst.sort()
        for i in range(len(lst)):
            if i>lst[i]:
                return i
        return len(dist)