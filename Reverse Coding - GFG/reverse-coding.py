#User function Template for python3

class Solution:
    def sumOfNaturals(self, n):
        # code here
        m=10**9+7
        ans=((n%m)*(((n%m)+(1%m))%m))%m
        return ans//2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.sumOfNaturals(n))
# } Driver Code Ends