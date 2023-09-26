class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Approach 1 - BF - check for all
        
        # Approach 2 - sort and do
        intervals.sort()
        res=[intervals[0]]
        j=0
        for i in range(1,len(intervals)):
            if(intervals[i][0]<=res[j][1]):
                res[j][1]=max(intervals[i][1],res[j][1])
            else:
                res.append(intervals[i])
                j+=1
        return res