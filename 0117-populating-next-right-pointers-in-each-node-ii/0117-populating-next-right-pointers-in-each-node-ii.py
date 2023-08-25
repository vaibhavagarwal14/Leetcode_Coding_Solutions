"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        root.next=None
        q=[]
        q.append(root)
        while len(q)!=0:
            lst=[]
            l=len(q)
            for i in range(l):
                node=q.pop(0)
                if node.left:
                    q.append(node.left)
                    lst.append(node.left)
                if node.right:
                    q.append(node.right)
                    lst.append(node.right)
            for i in range(len(lst)-1):
                lst[i].next=lst[i+1]
            if len(lst)!=0:
                lst[-1].next=None
        return root