#User function Template for python3

class Solution:
    def colName (self, n):
        # your code here
        ans=""
        
        while(n!=0):
            n-=1
            char=chr(n%26+ord('A'))
            ans=char+ans
            
            n//=26
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends