# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r=ListNode(0)
        d=ListNode(-1)
        d.next=r
        c=0
        while l1 and l2:
            t=l1.val+l2.val+c
            if t>9:
                temp=ListNode(t%10)
                c=t//10
            else:
                temp=ListNode(t)
                c=0
            r.next=temp    
            r=r.next
            l1=l1.next
            l2=l2.next
        if l1:
            while l1:
                t=l1.val+c
                if t>9:
                    temp=ListNode(t%10)
                    c=t//10
                else:
                    temp=ListNode(t)
                    c=0
                r.next=temp    
                r=r.next
                l1=l1.next
        elif l2:
            while l2:
                t=l2.val+c
                if t>9:
                    temp=ListNode(t%10)
                    c=t//10
                else:
                    temp=ListNode(t)
                    c=0
                r.next=temp    
                r=r.next
                l2=l2.next
        if c>0:
            temp=ListNode(c)
            r.next=temp
        return d.next.next
        