from typing import List


class Solution:
    def maxEqualSum(self, N1:int,N2:int,N3:int, S1 : List[int], S2 : List[int], S3 : List[int]) -> int:
        # code here
        s1=sum(S1)
        s2=sum(S2)
        s3=sum(S3)
        t1=t2=t3=0
        while(1):
            if(t1==N1 or t2==N2 or t3==N3):
                return 0
            elif(s1==s2 and s2==s3):
                return s1
            elif(s1>=s2 and s1>=s3):
                s1=s1-S1[t1]
                t1+=1
            elif(s2>=s3 and s2>=s1):
                s2=s2-S2[t2]
                t2+=1
            elif(s3>=s1 and s3>=s2):
                s3=s3-S3[t3]
                t3+=1
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(3)
        
        
        S1=IntArray().Input(a[0])
        
        
        S2=IntArray().Input(a[1])
        
        
        S3=IntArray().Input(a[2])
        
        obj = Solution()
        res = obj.maxEqualSum(a[0],a[1],a[2], S1, S2, S3)
        
        print(res)
        

# } Driver Code Ends