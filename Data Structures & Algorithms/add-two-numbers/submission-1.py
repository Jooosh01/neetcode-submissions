# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        dummy = ListNode()
        head = dummy
        r = 0
        while curr1 or curr2:
            v1 = 0
            v2 = 0
            if curr1:
                v1  = curr1.val
                curr1 = curr1.next
            if curr2:
                v2 = curr2.val
                curr2 = curr2.next
            nv = (v1+v2+r)%10
            dummy.next = ListNode(val=nv)
            dummy = dummy.next
            r = (v1+v2+r)//10
        if r > 0:
            dummy.next = ListNode(val=r)
        return head.next


        