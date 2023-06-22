#User function Template for python3


class Solution:
    def firstElementKTime(self,  a, n, k):
        # code here
        count={}
        for i in a:
            if(i in count):
                count[i]+=1
            else:
                count[i]=1
            if(count[i]==k):
                    return i
        return -1
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends