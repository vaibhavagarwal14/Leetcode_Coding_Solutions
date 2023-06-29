# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst=[]
        if len(lists)==0:
            return None
        for i in lists:
            curr=i
            while curr != None:
                lst.append(curr.val)
                curr=curr.next
        if(len(lst)==0):
            return None
        lst.sort()
        fin=ListNode(lst[0])
        curr=fin
        for i in range(1,len(lst)):
            curr.next=ListNode(lst[i])
            curr=curr.next
        return fin