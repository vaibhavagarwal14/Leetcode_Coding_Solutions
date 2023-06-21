#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):
        # Code here
        lst=[0,0,0]
        for i in bills:
            if(i==5):
                lst[0]+=1
            elif(i==10 and lst[0]!=0):
                lst[1]+=1
                lst[0]-=1
            elif(i==20 and lst[1]!=0 and lst[0]!=0):
                lst[2]+=1
                lst[1]-=1
                lst[0]-=1
            elif(i==20 and lst[0]>2):
                lst[2]+=1
                lst[0]-=3
            else:
                return False
        return True
                

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends