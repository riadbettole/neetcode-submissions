# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        setLink = set()
        
        while head :
            if head in setLink:
                return True
            setLink.add(head)
            head = head.next
            
        return False