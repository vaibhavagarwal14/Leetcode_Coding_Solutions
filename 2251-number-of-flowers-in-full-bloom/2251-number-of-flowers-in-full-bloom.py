class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # Approach 1
        # count={}
        # for i in people:
        #     if i in count:
        #         continue
        #     ct=0
        #     for j in flowers:
        #         if j[0]<=i and j[1]>=i:
        #             ct+=1
        #     count[i]=ct
        # ans=[]
        # for i in people:
        #     ans.append(count[i])
        # return ans
        
        # Approach 2
        starts = sorted(s for s, _ in flowers)
        ends = sorted(e for _, e in flowers)
        return [bisect.bisect_right(starts, person) -
            bisect.bisect_left(ends, person)
            for person in people]