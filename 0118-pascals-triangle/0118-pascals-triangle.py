class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Approach 1 - BF - nCr - O(n*n*r)
        # Approach 2 - Generating individual rows using nCr(better) - O(n^2)
        def generateRow(row):
            temp=[1]
            ans=1
            for col in range(1,row):
                ans=ans*(row-col)
                ans=ans//col
                temp.append(ans)
            return temp
        ans=[]
        for i in range(numRows):
            ans.append(generateRow(i+1))
        return ans