#User function Template for python3

class Solution:
    def maxOnes(self, a, n):
        # Your code goes here
        sum,mx=0,0
        cnt1=0
        
        for i in range(n):
            sum+=1 if a[i]==0 else (-1)
            
            if(a[i]==1): 
                cnt1+=1
            
            mx=max(mx,sum)
            
            if(sum<0): 
                sum=0
            
        return cnt1+mx

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maxOnes(a, n))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends