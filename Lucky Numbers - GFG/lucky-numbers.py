#User function Template for python3

class Solution:
    def isLucky(self, n): 
        #RETURN True OR False
        def check(n,i):
            if(n<i): return True
            if(n%i==0): return False
            
            return check(n-n//i,i+1)
        
        return check(n,2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
# } Driver Code Ends