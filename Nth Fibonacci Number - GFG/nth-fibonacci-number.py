
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        if n==1:
            return 0
        if n==2:
            return 1
        m=1e9+7
        a=0
        b=1
        n-=2
        while(n>=0):
            c=(a%m+b%m)%m
            a=b
            b=c
            n-=1
        return int(b%m)



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends