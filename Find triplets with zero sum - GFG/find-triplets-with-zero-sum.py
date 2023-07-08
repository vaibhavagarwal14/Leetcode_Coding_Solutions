#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        #code here
        arr.sort()
 
        for i in range(len(arr) - 2):
            if i == 0 or (i > 0 and arr[i] != arr[i - 1]):
                lo = i + 1
                hi = len(arr) - 1
                sum = 0 - arr[i]


                while lo < hi:
                    if arr[lo] + arr[hi] == sum:
                        return 1


                    elif arr[lo] + arr[hi] < sum:
                        lo += 1
                    else:
                        hi -= 1
        return 0
 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        if(Solution().findTriplets(a,n)):
            print(1)
        else:
            print(0)
# } Driver Code Ends