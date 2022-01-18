# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d=headA
        t=headB
        
        c1=c2=0
        while d:
            d=d.next
            c1=c1+1
            
        while t:
            t=t.next
            c2=c2+1
            
        if c1>c2:
            r=headA
            x=c1-c2
            s=headB
        else:
            r=headB
            x=c2-c1
            s=headA
        while x and r:
            r=r.next
            x=x-1
        while r:
            if r==s:
                return r
            r=r.next
            s=s.next
            
        return r