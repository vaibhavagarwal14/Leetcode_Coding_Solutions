# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0
        n2=0
        i=0
        while(l1!=None):
            n1=(l1.val)*(10**i)+n1
            l1=l1.next
            i+=1
        i=0
        while(l2!=None):
            n2=(l2.val)*(10**i)+n2
            l2=l2.next
            i+=1
        print(n1,n2)
        fin=n1+n2
        llfin=ListNode(fin%10)
        fin//=10
        curr=llfin
        while fin!=0:
            curr.next=ListNode(fin%10)
            fin//=10
            curr=curr.next
        return llfin