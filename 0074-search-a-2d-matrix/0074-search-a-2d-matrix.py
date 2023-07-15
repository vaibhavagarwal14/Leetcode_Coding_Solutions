class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m=len(matrix)
        n=len(matrix[0])
        l=0
        h=m*n
        while(l<h):
            mid=(h+l)//2
            i=mid//n
            j=mid%n
            if(target==matrix[i][j]):
                return True
            elif(target>matrix[i][j]):
                l=mid+1
            else:
                h=mid
        return False
        
        