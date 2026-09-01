# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        start = None
        if curr1 and curr2:
            if curr1.val < curr2.val:
                start = curr1
            else:
                start = curr2
        elif not curr1:
            start = curr2
        else:
            start = curr1
        d = ListNode()
        while curr1 != None or curr2 != None:
            if curr1 and curr2:
                if curr1.val < curr2.val:
                    d.next = curr1
                    d = curr1
                    curr1 = curr1.next
                else:
                    d.next = curr2
                    d = curr2
                    curr2 = curr2.next
            elif not curr1:
                d.next = curr2
                d = curr2
                curr2 = curr2.next
            else:
                d.next = curr1
                d = curr1
                curr1 = curr1.next
        return start

        