#User function Template for python3


class Solution:
    
    #Function to find the nodes that are common in both BST.
    def findCommon(self, root1, root2):
        # code here
        s1 = []
        s2 = []
        lst=[]
        while 1:
 
        # append the Nodes of first
        # tree in stack s1
            if root1:
                s1.append(root1)
                root1 = root1.left
 
        # append the Nodes of second tree
        # in stack s2
            elif root2:
                s2.append(root2)
                root2 = root2.left
 
        # Both root1 and root2 are NULL here
            elif len(s1) != 0 and len(s2) != 0:
                root1 = s1[-1]
                root2 = s2[-1]
 
            # If current keys in two trees are same
                if root1.data == root2.data:
                    lst.append(root1.data)
                    s1.pop(-1)
                    s2.pop(-1)
 
                # move to the inorder successor
                    root1 = root1.right
                    root2 = root2.right
 
                elif root1.data < root2.data:
 
                # If Node of first tree is smaller, than
                # that of second tree, then its obvious
                # that the inorder successors of current
                # Node can have same value as that of the
                # second tree Node. Thus, we pop from s2
                    s1.pop(-1)
                    root1 = root1.right
 
                # root2 is set to NULL, because we need
                # new Nodes of tree 1
                    root2 = None
                elif root1.data > root2.data:
                    s2.pop(-1)
                    root2 = root2.right
                    root1 = None
 
        # Both roots and both stacks are empty
            else:
                break
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root1=buildTree(s)
        s=input()
        root2=buildTree(s)
        ob = Solution()
        res = ob.findCommon(root1, root2)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends