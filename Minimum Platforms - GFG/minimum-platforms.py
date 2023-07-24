#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
 
    # plat_needed indicates
    # number of platforms
    # needed at a time
        plat_needed = 1
        result = 1
        i = 1
        j = 0
 
    # Similar to merge in
    # merge sort to process
    # all events in sorted order
        while (i < n and j < n):
 
        # If next event in sorted
        # order is arrival,
        # increment count of
        # platforms needed
            if (arr[i] <= dep[j]):
 
                plat_needed += 1
                i += 1
 
        # Else decrement count
        # of platforms needed
            elif (arr[i] > dep[j]):
 
                plat_needed -= 1
                j += 1
 
        # Update result if needed
            if (plat_needed > result):
                result = plat_needed
 
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends