#User function Template for python3


class Solution:
    def nextHappy (self, N):
        # code here
        def happy(n):
            while True:
                if(n==1):
                    return True
                elif(n==4):
                    return False
                n=sum([int(digit)**2 for digit in str(n)])
        i=N+1
        while(1):
            if(happy(i)):
                return i
            i+=1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.nextHappy(N))
# } Driver Code Ends