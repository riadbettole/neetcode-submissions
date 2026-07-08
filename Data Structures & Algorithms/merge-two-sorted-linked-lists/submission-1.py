# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        newList = ListNode(0, None)
        currNew = newList

        while curr1 and curr2:
            if curr1.val < curr2.val:
                currNew.next = curr1
                curr1 = curr1.next
            else:
                currNew.next = curr2
                curr2 = curr2.next
            currNew = currNew.next 

        if curr1:
            currNew.next = curr1
        else:
            currNew.next = curr2

        return newList.next