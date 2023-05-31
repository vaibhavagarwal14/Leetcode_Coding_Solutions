#User function Template for python3

class Solution:
    def reversedBits(self, X):
        # code here 
        num=0
        for i in range(32):
            num<<=1
            if X&1:
                num^=1
            X>>=1
        return num


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends