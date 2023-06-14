//{ Driver Code Starts

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
  public:
    long long maxDiamonds(int A[], int N, int K) {
        // code here
        priority_queue<int> pq;
        for (int i = 0; i < N; i++) {
        pq.push(A[i]);
        }
 
    // Stores the required result
    long long ans = 0;
 
    // Loop while the queue is not
    // empty and K is positive
    while (!pq.empty() && K--) {
 
        // Store the top element
        // from the pq
        int top = pq.top();
 
        // Pop it from the pq
        pq.pop();
 
        // Add it to the answer
        ans += top;
 
        // Divide it by 2 and push it
        // back to the pq
        top = top / 2;
        pq.push(top);
    }
    return ans;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N,K;
        
        cin>>N>>K;
        int A[N];
        
        for(int i=0; i<N; i++)
            cin>>A[i];

        Solution ob;
        cout << ob.maxDiamonds(A,N,K) << endl;
    }
    return 0;
}
// } Driver Code Ends